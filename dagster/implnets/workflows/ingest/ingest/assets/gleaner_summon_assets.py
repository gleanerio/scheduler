# a test asset to see that all the resource configurations load.
# basically runs the first step, of gleaner on geocodes demo datasets
from typing import Any
import json
import pandas as pd
import csv

from dagster import (
    asset, Config, Output,AssetKey,
    define_asset_job, AssetSelection,
get_dagster_logger,BackfillPolicy
)
from ec.datastore import s3 as utils_s3

from .gleaner_sources import sources_partitions_def
from ..utils import PythonMinioAddress

from ec.gleanerio.gleaner import getGleaner, getSitemapSourcesFromGleaner, endpointUpdateNamespace
from ec.reporting.report import missingReport, generateIdentifierRepo, generateGraphReportsRelease
from ec.graph.release_graph import ReleaseGraph
from ec.summarize import summaryDF2ttl, get_summary4graph, get_summary4repoSubset

SUMMARY_PATH = 'graphs/summary'
RELEASE_PATH = 'graphs/latest'

class HarvestOpConfig(Config):
    source_name: str
# sources_partitions_def = StaticPartitionsDefinition(
#     ["geocodes_demo_datasets", "iris"]
# )

def getSource(context, source_name):
    sources = context.repository_def.load_asset_value(AssetKey(["ingest","sources_all"]))
    source = list(filter(lambda t: t["name"]==source_name, sources))
    return source[0]

@asset(group_name="load",
key_prefix="ingest",
      deps=[AssetKey(["ingest","sources_names_active"]) ],
       partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
 #   , backfill_policy=BackfillPolicy.single_run()
       )
#@asset( required_resource_keys={"gleanerio"})
def gleanerio_run(context ) -> Output[Any]:
    gleaner_resource =  context.resources.gleanerio
    source= context.asset_partition_key_for_output()
    gleaner = gleaner_resource.execute(context, "gleaner", source )

    metadata={
                "source": source,  # Metadata can be any key-value pair
                "run": "gleaner",
                # The `MetadataValue` class has useful static methods to build Metadata
            }

    return Output(gleaner, metadata=metadata)
@asset(group_name="load",
key_prefix="ingest",
       deps=[gleanerio_run],
       partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
  #     ,backfill_policy=BackfillPolicy.single_run()
     )
#@asset(required_resource_keys={"gleanerio"})
def release_nabu_run(context) -> Output[Any]:
    gleaner_resource = context.resources.gleanerio
    source= context.asset_partition_key_for_output()
    nabu=gleaner_resource.execute(context, "release", source )
    metadata={
                "source": source,  # Metadata can be any key-value pair
                "run": "release",
                 "bucket_name": gleaner_resource.gs3.GLEANERIO_MINIO_BUCKET,  # Metadata can be any key-value pair
                 "object_name": f"{RELEASE_PATH}{source}"
                # The `MetadataValue` class has useful static methods to build Metadata
            }

    return Output(nabu, metadata=metadata)
''' Return results of summoning the JSON-LD SOS from a source.
This includes the number of url in the sitemap, how many jsonLD were 'summoned'
There may be multiple json-ld per web page, so this needs to be monitored over time.
And how many made it into milled (this is how good the conversion at a single jsonld to RDF is.

'''

@asset(
key_prefix="ingest",
    group_name="load",
       deps=[gleanerio_run], partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
  #  , backfill_policy=BackfillPolicy.single_run()
)
def load_report_s3(context):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 =  context.resources.gleanerio.gs3
    source_name = context.asset_partition_key_for_output()
    # source = getSitemapSourcesFromGleaner(gleaner_resource.GLEANERIO_GLEANER_CONFIG_PATH, sourcename=source_name)
    source = getSource(context, source_name)
    source_url = source.get('url')
    s3Minio = utils_s3.MinioDatastore(PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS,
                                                          gleaner_s3.GLEANERIO_MINIO_PORT),
                                       gleaner_s3.MinioOptions()
                                      )
    bucket = gleaner_s3.GLEANERIO_MINIO_BUCKET

    graphendpoint = None
    milled = False
    summon = True
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=summon)
    r = str('load repoort returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)
    s3Minio.putReportFile(bucket, source_name, "load_report_s3.json", report)
    get_dagster_logger().info(f"load s3 report  returned  {r} ")
    return


''' Return results of what  JSON-LD SOS is the S3 store, and compares it to the 'Named' graphs
in the graph store. This extends the load report s3.
This includes the number of url in the sitemap, how many jsonLD were 'summoned'
There may be multiple json-ld per web page, so this needs to be monitored over time.
And how many made it into milled (this is how good the conversion at a single jsonld to RDF is.
It then compares what identifiers are in the S3 store (summon path), and the Named Graph URI's
'''

@asset(
key_prefix="ingest",
    group_name="load",
       deps=[release_nabu_run], partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
  #  , backfill_policy=BackfillPolicy.single_run()
)
def load_report_graph(context):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 =  context.resources.gleanerio.gs3
    gleaner_triplestore = context.resources.gleanerio.triplestore

    source_name = context.asset_partition_key_for_output()
    # source = getSitemapSourcesFromGleaner(gleaner_resource.GLEANERIO_GLEANER_CONFIG_PATH, sourcename=source_name)
    source = getSource(context, source_name)
    source_url = source.get('url')
    s3Minio = utils_s3.MinioDatastore(PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS,
                                                          gleaner_s3.GLEANERIO_MINIO_PORT),
                                       gleaner_s3.MinioOptions()
                                      )
    bucket = gleaner_s3.GLEANERIO_MINIO_BUCKET

    graphendpoint = gleaner_triplestore.GraphEndpoint(gleaner_resource.GLEANERIO_GRAPH_NAMESPACE)
    milled = False
    summon = True
    returned_value = missingReport(source_url, bucket, source_name, s3Minio, graphendpoint, milled=milled, summon=False) # summon false. we want the graph
    r = str('load repoort graph returned value:{}'.format(returned_value))
    report = json.dumps(returned_value, indent=2)
    s3Minio.putReportFile(bucket, source_name, "load_report_graph.json", report)
    get_dagster_logger().info(f"load  report to graph returned  {r} ")
    return
class S3ObjectInfo:
    bucket_name=""
    object_name=""
@asset(group_name="load",key_prefix="ingest",
       name="release_summarize",
       deps=[release_nabu_run], partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
   # , backfill_policy=BackfillPolicy.single_run()
       )
def release_summarize(context) :
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 =  context.resources.gleanerio.gs3
    triplestore =context.resources.gleanerio.triplestore
    source_name = context.asset_partition_key_for_output()
    #source = getSitemapSourcesFromGleaner(gleaner_resource.GLEANERIO_GLEANER_CONFIG_PATH, sourcename=source_name)
    source = getSource(context,source_name)
    source_url = source.get('url')
    s3Minio = utils_s3.MinioDatastore(PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS,
                                                          gleaner_s3.GLEANERIO_MINIO_PORT),
                                       gleaner_s3.MinioOptions()
                                      )
    bucket = gleaner_s3.GLEANERIO_MINIO_BUCKET

   # endpoint = triplestore.GraphEndpoint# getting data, not uploading data
    #summary_namespace = _graphSummaryEndpoint()

    try:

        # summarydf = get_summary4repoSubset(endpoint, source_name)
        rg = ReleaseGraph()
        rg.read_release(PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS,
                                                          gleaner_s3.GLEANERIO_MINIO_PORT),
                        bucket,
                        source_name,
                        options=gleaner_s3.MinioOptions())
        summarydf = rg.summarize()
        nt, g = summaryDF2ttl(summarydf, source_name)  # let's try the new generator
        summaryttl = g.serialize(format='longturtle')
        # Lets always write out file to s3, and insert as a separate process
        # we might be able to make this an asset..., but would need to be acessible by http
        # if not stored in s3
        objectname = f"{SUMMARY_PATH}/{source_name}_release.ttl"  # needs to match that is expected by post
        s3ObjectInfo = S3ObjectInfo()
        s3ObjectInfo.bucket_name = bucket
        s3ObjectInfo.object_name = objectname

        bucket_name, object_name =s3Minio.putTextFileToStore(summaryttl, s3ObjectInfo)
        context.add_output_metadata(
            metadata={
                "source": source,  # Metadata can be any key-value pair
                "run": "release_summarize",
                "bucket_name": bucket_name,  # Metadata can be any key-value pair
                "object_name": object_name,
                # The `MetadataValue` class has useful static methods to build Metadata
            }
        )
        # inserted = sumnsgraph.insert(bytes(summaryttl, 'utf-8'), content_type="application/x-turtle")
        # if not inserted:
        #    raise Exception("Loading to graph failed.")
    except Exception as e:
        # use dagster logger
        get_dagster_logger().error(f"Summary. Issue creating graph  {str(e)} ")
        raise Exception(f"Loading Summary graph failed. {str(e)}")
        return 1

    return

@asset(group_name="load",key_prefix="ingest",
       deps=[gleanerio_run],
       partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
   # , backfill_policy=BackfillPolicy.single_run()
       )
def identifier_stats(context):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 =  context.resources.gleanerio.gs3
    triplestore =context.resources.gleanerio.triplestore
    source_name = context.asset_partition_key_for_output()
    # source = getSitemapSourcesFromGleaner(gleaner_resource.GLEANERIO_GLEANER_CONFIG_PATH, sourcename=source_name)
    source = getSource(context, source_name)
    source_url = source.get('url')
    s3Minio = utils_s3.MinioDatastore(PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS,
                                                          gleaner_s3.GLEANERIO_MINIO_PORT),
                                       gleaner_s3.MinioOptions()
                                      )
    bucket = gleaner_s3.GLEANERIO_MINIO_BUCKET


    returned_value = generateIdentifierRepo(source_name, bucket, s3Minio)
    r = str('returned value:{}'.format(returned_value))
    #r = str('identifier stats returned value:{}'.format(returned_value))
    report = returned_value.to_json()
    s3Minio.putReportFile(bucket, source_name, "identifier_stats.json", report)
    get_dagster_logger().info(f"identifer stats report  returned  {r} ")
    return

@asset(group_name="load",key_prefix="ingest",
       deps=[gleanerio_run],
       partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
   # , backfill_policy=BackfillPolicy.single_run()
       )
def bucket_urls(context):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 =  context.resources.gleanerio.gs3
    triplestore =context.resources.gleanerio.triplestore
    source_name = context.asset_partition_key_for_output()
    # source = getSitemapSourcesFromGleaner(gleaner_resource.GLEANERIO_GLEANER_CONFIG_PATH, sourcename=source_name)
    source = getSource(context, source_name)
    source_url = source.get('url')
    s3Minio = utils_s3.MinioDatastore(PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS,
                                                          gleaner_s3.GLEANERIO_MINIO_PORT),
                                       gleaner_s3.MinioOptions()
                                      )
    bucket = gleaner_s3.GLEANERIO_MINIO_BUCKET


    res = s3Minio.listSummonedUrls(bucket, source_name)
    r = str('returned value:{}'.format(res))
    bucketurls =  pd.DataFrame(res).to_csv(index=False, quoting=csv.QUOTE_NONNUMERIC)
    s3Minio.putReportFile(bucket, source_name, "bucketutil_urls.csv", bucketurls)
    get_dagster_logger().info(f"bucker urls report  returned  {r} ")
    return

# original code. inlined.
# def _releaseUrl( source, path=RELEASE_PATH, extension="nq"):
#     proto = "http"
#     if GLEANER_MINIO_USE_SSL:
#         proto = "https"
#     address = _pythonMinioAddress(GLEANER_MINIO_ADDRESS, GLEANER_MINIO_PORT)
#     bucket = GLEANER_MINIO_BUCKET
#     release_url = f"{proto}://{address}/{bucket}/{path}/{source}_release.{extension}"
#     return release_url
@asset(group_name="load",key_prefix="ingest",
       deps=[release_nabu_run],
       partitions_def=sources_partitions_def, required_resource_keys={"gleanerio"}
   # , backfill_policy=BackfillPolicy.single_run()
       )
def graph_stats_report(context) :
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    source_name = context.asset_partition_key_for_output()
    # source = getSitemapSourcesFromGleaner(gleaner_resource.GLEANERIO_GLEANER_CONFIG_PATH, sourcename=source_name)
    source = getSource(context, source_name)
    source_url = source.get('url')
    s3Minio = utils_s3.MinioDatastore(PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS,
                                                         gleaner_s3.GLEANERIO_MINIO_PORT),
                                      gleaner_s3.MinioOptions()
                                      )
    bucket = gleaner_s3.GLEANERIO_MINIO_BUCKET

    #returned_value = generateGraphReportsRepo(source_name,  graphendpoint, reportList=reportTypes["repo_detailed"])
    proto = "http"
    if gleaner_s3.GLEANERIO_MINIO_USE_SSL:
        proto = "https"
    address = PythonMinioAddress(gleaner_s3.GLEANERIO_MINIO_ADDRESS, gleaner_s3.GLEANERIO_MINIO_PORT)

    s3FileUrl = f"{proto}://{address}/{bucket}/{RELEASE_PATH}/{source_name}_release.nq"
    #s3FileUrl = _releaseUrl(source_name )
    get_dagster_logger().info(f"get release for {source_name} from   returned  {s3FileUrl} ")
    returned_value = generateGraphReportsRelease(source_name,s3FileUrl)
    r = str('returned value:{}'.format(returned_value))
    #report = json.dumps(returned_value, indent=2) # value already json.dumps
    report = returned_value
    s3Minio.putReportFile(bucket, source_name, "graph_stats.json", report)
    get_dagster_logger().info(f"graph stats  returned  {r} ")
    return

#might need to use this https://docs.dagster.io/_apidocs/repositories#dagster.RepositoryDefinition.get_asset_value_loader
#@sensor(job=summon_asset_job)
# @sensor(asset_selection=AssetSelection.keys("gleanerio_orgs"))
# def sources_sensor(context ):
#     sources =  gleanerio_orgs
#     new_sources = [
#         source
#         for source in sources
#         if not sources_partitions_def.has_partition_key(
#             source, dynamic_partitions_store=context.instance
#         )
#     ]
#
#     return SensorResult(
#         run_requests=[
#             RunRequest(partition_key=source) for source in new_sources
#         ],
#         dynamic_partitions_requests=[
#             sources_partitions_def.build_add_request(new_sources)
#         ],
#     )

# need to add a sensor to add paritions when one is added
# https://docs.dagster.io/concepts/partitions-schedules-sensors/partitioning-assets#dynamically-partitioned-assets


# #########
# CRUFT
#  worked to see if this could be a graph with an assent, and really a defiend asset job works better

# ## partitioning
# ####
# class HarvestOpConfig(Config):
#     source_name: str
# @dynamic_partitioned_config(partition_fn=gleanerio_orgs)
# def harvest_config(partition_key: str):
#     return {
#         "ops":
#             {"harvest_and_release":
#                  {"config": {"source_name": partition_key},
#                   "ops": {
#                       "gleanerio_run":
#                            {"config": {"source_name": partition_key}
#                             },
#                       "nabu_release_run":
#                            {"config": {"source_name": partition_key}
#                             }
#                   }
#                   }
#              }
#     }
#
# # ops:
# #   harvest_and_release:
# #     ops:
# #       gleanerio_run:
# #         config:
# #           source_name: ""
# #       nabu_release_run:
# #         config:
# #           source_name: ""
#
# @graph_asset(partitions_def=sources_partitions_def)
# #@graph_asset( )
# def harvest_and_release() :
#     #source = context.asset_partition_key_for_output()
#     #containers = getImage()
#     #harvest = gleanerio_run(start=containers)
#     harvest = gleanerio_run()
#     release = nabu_release_run(harvest)
#     return release
#
# #@asset
# # def harvest_op(context, config: HarvestOpConfig):
# #     context.log.info(config.source_name)
# #     harvest = gleanerio_run()
# #     release = nabu_release_run(harvest)
# #     return release
#
# # @job(config=harvest_config)
# # def harvest_job( ):
# #     harvest_op()
#     #harvest_and_release()
# # @schedule(cron_schedule="0 0 * * *", job=harvest_job)
# # def geocodes_schedule():
# #     return RunRequest(partition_key="iris")
