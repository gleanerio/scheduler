from dagster import (
op, job, Config,get_dagster_logger,DefaultSensorStatus,
sensor, RunRequest, RunConfig,
SensorEvaluationContext,
SkipReason,
AssetKey,
static_partitioned_config,
asset_sensor, EventLogEntry
)
from dagster_aws.s3.sensor import get_s3_keys
from typing import List, Dict
from pydantic import Field

from ..resources.gleanerio import GleanerioResource
from ..resources.gleanerS3 import gleanerS3Resource
from ..resources.graph import BlazegraphResource
from ..assets import tenant_partitions_def,TenantConfig
from ..jobs.tenant_load import  release_asset_job, create_graph_namespaces
from ..assets.gleaner_summon_assets import RELEASE_PATH, SUMMARY_PATH

#from ..jobs.tennant_load import  build_community
# This sensor needs to detect when an source has completed its' run
# and then load the data into the client's graphstore.



# #######
# Put the config for a tennant at the job level so we only have to define it once
######





#@sensor(job=build_community,minimum_interval_seconds=60)

# https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors#using-resources-in-sensors
# sensor factor example
# https://github.com/dagster-io/dagster/blob/master/examples/project_fully_featured/project_fully_featured/sensors/hn_tables_updated_sensor.py
######
# https://docs.dagster.io/concepts/partitions-schedules-sensors/asset-sensors#when-all-partitions-have-new-materializations
########
@asset_sensor(asset_key=AssetKey(["ingest","release_summarize"]),
       #       default_status=DefaultSensorStatus.RUNNING,
              job=release_asset_job, required_resource_keys={"gleanerio"},
            #  minimum_interval_seconds=3600
              )
def release_file_sensor(context,config: TenantConfig
                        ):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    since_key = context.cursor or None
    context.log.info(f"sinceKey: {since_key}")
    #new_s3_keys = get_s3_keys(gleaner_s3.GLEANERIO_MINIO_BUCKET, prefix=SUMMARY_PATH, since_key=since_key)
    if since_key is None:
        new_s3_keys = s3_resource.get_client().list_objects_v2(
            Bucket=gleaner_s3.GLEANERIO_MINIO_BUCKET,
            Prefix=SUMMARY_PATH
        )
    else:
        new_s3_keys = s3_resource.get_client().list_objects_v2(
        Bucket=gleaner_s3.GLEANERIO_MINIO_BUCKET,
        Prefix=SUMMARY_PATH,
        StartAfter=since_key
        )
    new_s3_keys = list(new_s3_keys)
    get_dagster_logger().info(f"keys: {new_s3_keys}")
    if not new_s3_keys:
        return SkipReason(f"No new s3 files found for bucket {gleaner_s3.GLEANERIO_MINIO_BUCKET}.")
    get_dagster_logger().info(f"new key len: {len(new_s3_keys)}")
    last_key = new_s3_keys[-1]

    run_requests = [RunRequest(run_key=s3_key, run_config={}) for s3_key in new_s3_keys]
    context.update_cursor(last_key)
    return run_requests
@asset_sensor(asset_key=AssetKey(["ingest","release_summarize"]),
              default_status=DefaultSensorStatus.RUNNING,
              job=release_asset_job, required_resource_keys={"gleanerio"},
            #  minimum_interval_seconds=3600
              )
def release_file_sensor_v2(context,asset_event: EventLogEntry
                        ):
    assert asset_event.dagster_event and asset_event.dagster_event.asset_key

    source_name = asset_event.dagster_event.partition
    source_key= asset_event.dagster_event.asset_key
    get_dagster_logger().info(f"partition_key: {source_name} source_key: {source_key}")

    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    since_key = context.cursor or None
    context.log.info(f"sinceKey: {since_key}")

    run_requests = [RunRequest(partition_key=source_name,run_key=f"{source_name}_upload_release_{since_key}", run_config={})]
    #context.update_cursor(since_key+1)
    context.update_cursor(since_key)
    context.log.info(f"sinceKey: {context.cursor}")
    return run_requests
