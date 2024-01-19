from dagster import (
op, job, Config,
sensor, RunRequest, RunConfig,
SensorEvaluationContext,asset_sensor, EventLogEntry,
SkipReason,
AssetKey,
static_partitioned_config
)
from dagster_aws.s3.sensor import get_s3_keys
from typing import List, Dict
from pydantic import Field

from ..resources.gleanerio import GleanerioResource
from ..resources.gleanerS3 import gleanerS3Resource
from ..resources.graph import BlazegraphResource

class TennantConfig(Config):
    source_name: str
    name: str
    source_list: List[str]
    TENNANT_GRAPH_NAMESPACE: str
    TENNANT_GRAPH_SUMMARY_NAMESPACE: str
    SUMMARY_PATH: str =  Field(
         description="GLEANERIO_GRAPH_SUMMARY_PATH.", default='graphs/summary')
    RELEASE_PATH : str =  Field(
         description="GLEANERIO_GRAPH_RELEASE_PATH.", default='graphs/latest')


class TennantOpConfig(Config):
    source_name: str
@op(required_resource_keys={"gleanerio",})
def upload_release(context, config:TennantOpConfig  ):
    context.log.info(config.source_name)
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
@op(required_resource_keys={"gleanerio",})
def upload_summary(context, config:TennantOpConfig):
    context.log.info(config.source_name)
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore

# #######
# Put the config for a tennant at the job level so we only have to define it once
######

TENNANT_NAMES = [
    "dev",
    "geocodesall",

]



@static_partitioned_config(partition_keys=TENNANT_NAMES)
def tennant_config(partition_key: str):

    # default_config ={"ops": {
    #     "upload_release":
    #         {"config":
    #             {
    #                 TennantConfig(
    #                     source_name=partition_key,
    #                     name="name",
    #                     source_list=[],
    #                     TENNANT_GRAPH_NAMESPACE="",
    #                     TENNANT_GRAPH_SUMMARY_NAMESPACE=""
    #                 )
    #             }
    #             }
    #         },
    #     "upload_summary":
    #         {"config":
    #             {
    #                 TennantConfig(
    #                 source_name=partition_key,
    #                 name="name",
    #                 source_list=[],
    #                 TENNANT_GRAPH_NAMESPACE="",
    #                 TENNANT_GRAPH_SUMMARY_NAMESPACE=""
    #                 )
    #             }
    #         }
    #     }
    default_config = {"ops": {
        {"upload_release": {"config": {"source_name": partition_key}}},
        {"upload_summary": {"config": {"source_name": partition_key}}}
    }}
    return default_config
    #return {"ops": {"continent_op": {"config": {"continent_name": partition_key}}}}
@job(config=tennant_config)
def build_community():
    upload_release()
    upload_summary()
#@sensor(job=build_community,minimum_interval_seconds=60)
@asset_sensor(asset_key=AssetKey("release_summarize"), job=build_community, required_resource_keys={"gleanerio"})
def release_file_sensor(context,config: TennantConfig, gleanerio:GleanerioResource,
                        minimum_interval_seconds=3600):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    since_key = context.cursor or None
    new_s3_keys = get_s3_keys(gleaner_s3.GLEANERIO_MINIO_BUCKET, prefix=config.RELEASE_PATH, since_key=since_key)
    if not new_s3_keys:
        return SkipReason(f"No new s3 files found for bucket {gleaner_s3.GLEANERIO_MINIO_BUCKET}.")
    last_key = new_s3_keys[-1]

    run_requests = [RunRequest(run_key=s3_key, run_config={}) for s3_key in new_s3_keys]
    context.update_cursor(last_key)
    return run_requests
