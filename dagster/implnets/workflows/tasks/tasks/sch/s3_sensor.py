from dagster import(
    op, job, Config, get_dagster_logger,
    sensor, RunRequest, RunConfig,
    SensorEvaluationContext, asset_sensor, EventLogEntry,
    SkipReason,
    AssetKey,
    static_partitioned_config,
    DefaultSensorStatus
)
from dagster_aws.s3.sensor import get_s3_keys

from ..jobs.jobs import tenant_asset_job

@sensor(name="s3_config_source_sensor",
    default_status=DefaultSensorStatus.RUNNING,
    #, job_name="sources_updated_job",
        job=tenant_asset_job,
     required_resource_keys={"s3"},
            #  minimum_interval_seconds=3600
              )
def tenant_s3_sensor(context
                        ):

    gleaner_s3 = context.resources.s3

    since_key = context.cursor or None
    get_dagster_logger().info(f"sinceKey: {since_key}")
    config_path=(f"{gleaner_s3.GLEANERIO_CONFIG_PATH}")
    filename = f"{gleaner_s3.GLEANERIO_CONFIG_PATH}{gleaner_s3.GLEANERIO_TENANT_FILENAME}"
    new_s3_keys = gleaner_s3.s3.get_client().head_object(
            Bucket=gleaner_s3.GLEANERIO_MINIO_BUCKET,
            Key=filename,

        )
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
