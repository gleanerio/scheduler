import json
from typing import Any
import yaml
import os
import pandas as pd
from pydash import pick
from dagster import (asset,
                     get_dagster_logger,
                     Output,
                     DynamicPartitionsDefinition,
                     define_asset_job,
                    AssetSelection,
                    sensor,SensorResult,
                    RunRequest,
asset_sensor, AssetKey,
                     )

@asset(required_resource_keys={"triplestore"})
def tennant_sources(context ) ->Any:
    s3_resource = context.resources.triplestore.s3

    t=s3_resource.getTennatInfo()
    tennants = t['tennant']
    listTennants = map (lambda a: {a['community']}, tennants)
    get_dagster_logger().info(str(t))

    return t
        #     metadata={
        #         "tennants": str(listTennants),  # Metadata can be any key-value pair
        #         "run": "gleaner",
        #         # The `MetadataValue` class has useful static methods to build Metadata
        #     }
        # )
@asset(required_resource_keys={"triplestore"})
def tennant_names(context, tennant_sources ) -> Output[Any]:

    tennants = tennant_sources['tennant']
    listTennants = map (lambda a: {a['community']}, tennants)
    get_dagster_logger().info(str(listTennants))
    communities = list(listTennants)
    return Output(
            communities,
            metadata={
                "tennants": str(listTennants),  # Metadata can be any key-value pair
                "run": "gleaner",
                # The `MetadataValue` class has useful static methods to build Metadata
            }
        )


community_partitions_def = DynamicPartitionsDefinition(name="tennant_names")
tennant_job = define_asset_job(
    "tennant_job", AssetSelection.keys("tennant_names"), partitions_def=community_partitions_def
)
#@sensor(job=tennant_job)
@asset_sensor(asset_key=AssetKey("tennant_names"), job=tennant_job)
def community_sensor(context):
    new_community = [
        community
        for community in tennant_names
        if not context.instance.has_dynamic_partition(
            community_partitions_def.name, community
        )
    ]

    return SensorResult(
        run_requests=[
            RunRequest(partition_key=community) for community in new_community
        ],
        dynamic_partitions_requests=[
            community_partitions_def.build_add_request(new_community)
        ],
    )
REPORT_PATH = "reports/"
COMMUNITY_PATH = "reports/community/"
TASKS_PATH="tasks/"
ORG_PATH = "orgs/"
STAT_FILE_NAME = "missing_report_graph.json"

def _pythonMinioUrl(url):

    if (url.endswith(".amazonaws.com")):
        PYTHON_MINIO_URL = "s3.amazonaws.com"
    else:
        PYTHON_MINIO_URL = url
    return PYTHON_MINIO_URL

def getName(name):
    return name.replace("orgs/","").replace(".nq","")
# @asset(group_name="community")
# def source_list(tennant_sources) -> Output(str):
#     s3Minio = s3.MinioDatastore(_pythonMinioUrl(GLEANER_MINIO_ADDRESS), MINIO_OPTIONS)
#     orglist = s3Minio.listPath(GLEANER_MINIO_BUCKET, ORG_PATH,recursive=False)
#     sources = map( lambda f: { "name": getName(f.object_name)}, orglist )
#     source_json = json.dumps(list(sources))
#     os.makedirs("data", exist_ok=True)
#
#     s3Minio.putReportFile(GLEANER_MINIO_BUCKET, "all", f"source_list.json", source_json )
#     with open("data/source_list.json", "w") as f:
#         json.dump(list(sources), f)
#     return source_json
#@asset(deps=[source_list])

# set a prefix so we can have some named stats file

#@asset( group_name="load")
@asset(partitions_def=community_partitions_def,
     #  deps=[tennant_sources],
       group_name="community",
       required_resource_keys={"triplestore"} )
def loadstatsCommunity(context, tennant_sources) -> str:
    prefix="history"
    logger = get_dagster_logger()
    s3 = context.resources.triplestore.s3
    s3Client = context.resources.triplestore.s3.get_client()
 #   sourcelist = list(s3Minio.listPath(GLEANER_MINIO_BUCKET, ORG_PATH,recursive=False))
    community_code= context.asset_partition_key_for_output()
    stats = []
    try:
        ts = tennant_sources
        t =list(filter ( lambda a: a['community']== community_code, ts["tennant"] ))
        s = t[0]["sources"]
        for source in s:

            dirs = s3.listPath(path=f"{REPORT_PATH}{source}/")


            for d in dirs:
                latestpath = f"{REPORT_PATH}{source}/latest/"
                if (d.object_name.casefold() == latestpath.casefold()) or (d.is_dir == False):
                    continue
                path = f"/{d.object_name}{STAT_FILE_NAME}"

                try:
                    resp = s3Client.getFile(path=path)
                    stat = json.loads(resp)
                    stat = pick(stat, 'source', 'sitemap', 'date', 'sitemap_count', 'summoned_count',
                                'missing_sitemap_summon_count',
                                'graph_urn_count', 'missing_summon_graph_count')
                    stats.append(stat)
                except Exception as ex:
                    get_dagster_logger().info(f"Failed to get source {source} for tennant {community_code}  {ex}")
    except Exception as ex:
        get_dagster_logger().info(f"Failed to get tennat {community_code}  {ex}")
    # for source in tennant_sources["tennant"]:
    #     try:
    #        # stat = s3Minio.getReportFile(GLEANER_MINIO_BUCKET,source.get("name"), STAT_FILE_NAME )
    #        repo = community_code
    #        dirs = s3Minio.listPath( path=f"{REPORT_PATH}{repo}/",recursive=False )
    #        for d in dirs:
    #            latestpath = f"{REPORT_PATH}{repo}/latest/"
    #            if (d.object_name.casefold() == latestpath.casefold()) or (d.is_dir == False):
    #                continue
    #            path = f"/{d.object_name}{STAT_FILE_NAME}"
    #
    #            try:
    #                resp = s3Minio.getFile(path=path)
    #                stat = json.loads(resp)
    #                stat = pick(stat, 'source', 'sitemap', 'date', 'sitemap_count', 'summoned_count',
    #                            'missing_sitemap_summon_count',
    #                            'graph_urn_count', 'missing_summon_graph_count')
    #                stats.append(stat)
    #            except Exception as ex:
    #                logger.info(f"no missing graph report {source.get('name')}  {ex}")
    #     except Exception as ex:
    #         logger.info(f"Failed to get { source.get('name')}  {ex}")
    df = pd.DataFrame(stats)
    os.mkdir(f"data/{community_code}")
    df.to_csv(f"data/{community_code}/all_stats.csv")
    df_csv = df.to_csv()
    # humm, should we just have an EC utils resource
    #s3Minio.putReportFile(GLEANER_MINIO_BUCKET, "all", f"all_stats.csv", df_csv)
    get_dagster_logger().info(f"all_stats.csv uploaded ")
    return df_csv
