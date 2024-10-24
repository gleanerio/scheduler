from dagster import (
op, job, Config,get_dagster_logger,
sensor, RunRequest, RunConfig,
SensorEvaluationContext,asset_sensor, EventLogEntry,
SkipReason,
AssetKey,
static_partitioned_config,
DefaultSensorStatus
)
from dagster_aws.s3.sensor import get_s3_keys
from typing import List, Dict
from pydantic import Field

from ..resources.gleanerio import GleanerioResource
from ..resources.gleanerS3 import gleanerS3Resource
from ..resources.graph import BlazegraphResource
from ..assets import tenant_partitions_def,TenantConfig
from ..jobs.tenant_load import  (release_asset_job, create_graph_namespaces, tenant_asset_job)
from ..jobs.summon_assets import sources_asset_job
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
@sensor(name="s3_config_source_sensor",
    default_status=DefaultSensorStatus.RUNNING,
    #, job_name="sources_updated_job",
        job=sources_asset_job,
     required_resource_keys={"gleanerio"},
            #  minimum_interval_seconds=3600
              )
def sources_s3_sensor(context
                        ):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    since_key = context.cursor or None
    get_dagster_logger().info(f"sinceKey: {since_key}")
    config_path=f"{gleaner_s3.GLEANERIO_CONFIG_PATH}"
    filename = f"{gleaner_s3.GLEANERIO_CONFIG_PATH}{gleaner_s3.GLEANERIO_SOURCES_FILENAME}"

    new_s3_keys = s3_resource.get_client().head_object(
            Bucket=gleaner_s3.GLEANERIO_MINIO_BUCKET,
            Key=filename,

        )

    # new_s3_keys = s3_resource.resource.ObjectSummary(
    #     Bucket=gleaner_s3.GLEANERIO_MINIO_BUCKET,
    #     Key=filename,
    #
    # )

    # since_key = context.cursor or None
   # new_s3_keys = get_s3_keys("my_s3_bucket", since_key=since_key)

    if not new_s3_keys:
        return SkipReason(f"No new s3 files found for bucket {gleaner_s3.GLEANERIO_MINIO_BUCKET}. {filename}")
    get_dagster_logger().info(f"metadata {new_s3_keys}")
    #new_s3_keys = list(new_s3_keys)
    last_key = str(new_s3_keys['LastModified'])
    get_dagster_logger().info(f"last_modified: {last_key}")
    run_requests =[]
    if since_key is None or  since_key < last_key:
        #run_requests = [RunRequest(run_key=s3_key, run_config={}) for s3_key in new_s3_keys]
        run_requests = [RunRequest(run_key=last_key, run_config={})]
        context.update_cursor(last_key)
    return run_requests

@sensor(name="s3_configs_tenant__sensor",
    default_status=DefaultSensorStatus.RUNNING,
    #, job_name="sources_updated_job",
        job=tenant_asset_job,
     required_resource_keys={"gleanerio"},
            #  minimum_interval_seconds=3600
              )
def tenant_s3_sensor(context
                        ):
    gleaner_resource = context.resources.gleanerio
    s3_resource = context.resources.gleanerio.gs3.s3
    gleaner_s3 = context.resources.gleanerio.gs3
    triplestore = context.resources.gleanerio.triplestore
    since_key = context.cursor or None
    get_dagster_logger().info(f"sinceKey: {since_key}")
    config_path=f"{gleaner_s3.GLEANERIO_CONFIG_PATH}"
    filename = f"{gleaner_s3.GLEANERIO_CONFIG_PATH}{gleaner_s3.GLEANERIO_TENANT_FILENAME}"

    new_s3_keys = s3_resource.get_client().head_object(
            Bucket=gleaner_s3.GLEANERIO_MINIO_BUCKET,
            Key=filename,

        )

    # new_s3_keys = s3_resource.resource.ObjectSummary(
    #     Bucket=gleaner_s3.GLEANERIO_MINIO_BUCKET,
    #     Key=filename,
    #
    # )

    # since_key = context.cursor or None
   # new_s3_keys = get_s3_keys("my_s3_bucket", since_key=since_key)

    if not new_s3_keys:
        return SkipReason(f"No new s3 files found for bucket {gleaner_s3.GLEANERIO_MINIO_BUCKET}. {filename}")
    get_dagster_logger().info(f"metadata {new_s3_keys}")
    #new_s3_keys = list(new_s3_keys)
    last_key = str(new_s3_keys['LastModified'])
    get_dagster_logger().info(f"last_modified: {last_key}")
    run_requests =[]
    if since_key is None or  since_key < last_key:
        #run_requests = [RunRequest(run_key=s3_key, run_config={}) for s3_key in new_s3_keys]
        run_requests = [RunRequest(run_key=last_key, run_config={})]
        context.update_cursor(last_key)
    return run_requests
