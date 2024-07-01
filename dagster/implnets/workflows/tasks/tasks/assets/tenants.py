import json
from typing import Any
from io import StringIO
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
                    sensor,SensorResult,DefaultSensorStatus,
                    RunRequest,
asset_sensor, AssetKey,
                     )
from ec.datastore import s3
from distutils import util
from ..resources.gleanerS3 import _pythonMinioAddress

GLEANER_MINIO_ADDRESS = os.environ.get('GLEANERIO_MINIO_ADDRESS')
GLEANER_MINIO_PORT = os.environ.get('GLEANERIO_MINIO_PORT')
GLEANER_MINIO_USE_SSL = bool(util.strtobool(os.environ.get('GLEANERIO_MINIO_USE_SSL', 'true')))
GLEANER_MINIO_SECRET_KEY = os.environ.get('GLEANERIO_MINIO_SECRET_KEY')
GLEANER_MINIO_ACCESS_KEY = os.environ.get('GLEANERIO_MINIO_ACCESS_KEY')
GLEANER_MINIO_BUCKET = os.environ.get('GLEANERIO_MINIO_BUCKET')

MINIO_OPTIONS={"secure":GLEANER_MINIO_USE_SSL

              ,"access_key": GLEANER_MINIO_ACCESS_KEY
              ,"secret_key": GLEANER_MINIO_SECRET_KEY
               }
@asset(group_name="community",key_prefix="task",
       required_resource_keys={"triplestore"})
def task_tenant_sources(context) ->Any:
    s3_resource = context.resources.triplestore.s3

    t=s3_resource.getTennatInfo()
    tenants = t['tenant']
    listTenants = map (lambda a: {a['community']}, tenants)
    get_dagster_logger().info(str(t))

    return t
        #     metadata={
        #         "tennants": str(listTenants),  # Metadata can be any key-value pair
        #         "run": "gleaner",
        #         # The `MetadataValue` class has useful static methods to build Metadata
        #     }
        # )
@asset(group_name="community",key_prefix="task",
       #name='task_tenant_names',
       required_resource_keys={"triplestore"})
def task_tenant_names(context, task_tenant_sources) -> Output[Any]:

    tenants = task_tenant_sources['tenant']
    listTenants = map (lambda a: a['community'], tenants)
    get_dagster_logger().info(str(listTenants))
    communities = list(listTenants)
    return Output(
            communities,
            metadata={
                "tenants": str(listTenants),  # Metadata can be any key-value pair
                "run": "gleaner",
                # The `MetadataValue` class has useful static methods to build Metadata
            }
        )


community_partitions_def = DynamicPartitionsDefinition(name="tenantsPartition")
tenant_task_job = define_asset_job(
    "tenant_job", AssetSelection.keys(AssetKey(["task","loadstatsCommunity"])), partitions_def=community_partitions_def
)
#@sensor(job=tenant_job)
@asset_sensor(asset_key=AssetKey(["task","task_tenant_names"]),
               default_status=DefaultSensorStatus.RUNNING,
     job=tenant_task_job)
def community_sensor(context):
    tenants = context.repository_def.load_asset_value(AssetKey(["task","task_tenant_names"]))
    new_community = [
        community
        for community in tenants
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
# def source_list(task_tenant_sources) -> Output(str):
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
      deps=[AssetKey(["task","task_tenant_sources"])],
       group_name="community",
        key_prefix="task",
       required_resource_keys={"triplestore"} )
def loadstatsCommunity(context, task_tenant_sources) -> str:
    prefix="history"
    logger = get_dagster_logger()
    s3_config = context.resources.triplestore.s3
    s3Client = context.resources.triplestore.s3.s3.get_client()
    s3Minio = s3.MinioDatastore(_pythonMinioUrl(s3_config.GLEANERIO_MINIO_ADDRESS), MINIO_OPTIONS)
 #   sourcelist = list(s3Minio.listPath(GLEANER_MINIO_BUCKET, ORG_PATH,recursive=False))
    community_code= context.asset_partition_key_for_output()
    stats = []
    try:
        ts = task_tenant_sources
        t =list(filter ( lambda a: a['community']== community_code, ts["tenant"] ))
        s = t[0]["sources"]
        for source in s:

            dirs = s3Minio.listPath(path=f"{REPORT_PATH}{source}/",recursive=False )


            for d in dirs:
                latestpath = f"{REPORT_PATH}{source}/latest/"
                # minio reference
                # if (d.object_name.casefold() == latestpath.casefold()) or (d.is_dir == False):
                #     continue
                # path = f"/{d.object_name}{STAT_FILE_NAME}"
                if (d['Key'].casefold() == latestpath.casefold()) or (d.is_dir == False) :
                    continue
                path = f"/{d['Key']}{STAT_FILE_NAME}"

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
        context.log.info(f"Failed to get tenant {community_code}  {ex}")
    # for source in task_tenant_sources["tennant"]:
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
    context.log.info(stats)
    df = pd.DataFrame(stats)
    context.log.info(df)
    # try:
    #     os.mkdir(f"data/{community_code}")
    # except FileExistsError:
    #     logger.debug(f"directory data/{community_code} exists")
    # except FileNotFoundError:
    #     logger.error(f"error creating directory. Fix community name.  'data/{community_code}' ")
    #df.to_csv(f"data/{community_code}/all_stats.csv")

    df_csv = df.to_csv()

    # stringio = StringIO(df_csv)
    # s3Client.upload_fileobj(stringio, s3_config.GLEANERIO_MINIO_BUCKET, f"data/{community_code}/all_stats.csv")
    # humm, should we just have an EC utils resource
    s3Minio.putReportFile(s3_config.GLEANERIO_MINIO_BUCKET, f"tenant/{community_code}", f"all_stats.csv", df_csv)
    # with open(stringio, "rb") as f:
    #     s3.upload_fileobj(f, s3.GLEANERIO_MINIO_BUCKET, f"data/all/all_stats.csv")
    context.log.info(f"all_stats.csv uploaded ")
    #return df_csv # now checking return types
    return df_csv
