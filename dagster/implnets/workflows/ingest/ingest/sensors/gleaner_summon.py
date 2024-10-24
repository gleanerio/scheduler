import os

import dagster
from dagster import (
    SensorResult, RunRequest,
    EventLogEntry, AssetKey, asset_sensor,
    schedule,ScheduleDefinition,DefaultSensorStatus,DefaultScheduleStatus,
get_dagster_logger
)
from ..assets import (
 sources_partitions_def
)
from ..jobs.summon_assets import summon_asset_job


# this monitors the asset. It will harvest a new source
# the sources_schedule_sensor will add to the weekly schedule

# note on removal of partitions https://github.com/dagster-io/dagster/issues/14026
@asset_sensor(default_status=DefaultSensorStatus.RUNNING, asset_key=AssetKey(["ingest","sources_names_active"]), job=summon_asset_job
   # , minimum_interval_seconds=600
               )
def sources_sensor(context,  asset_event: EventLogEntry):
    context.log.info(f"sources_sensor: start")
    assert asset_event.dagster_event and asset_event.dagster_event.asset_key
    context.log.info(f"asset_key {asset_event.dagster_event.asset_key}")
# well this is a pain. but it works. Cannot just pass it like you do in ops
    # otherwise it's just an AssetDefinition.
    sources = context.repository_def.load_asset_value(AssetKey(["ingest","sources_names_active"]))
    new_sources = [
        source
        for source in sources
        if not sources_partitions_def.has_partition_key(
            source, dynamic_partitions_store=context.instance
        )
    ]
    removed_sources = [
        source
        for source in sources_partitions_def.get_partition_keys(dynamic_partitions_store=context.instance)
        if not source in sources
    ]
    for s in removed_sources:
        context.instance.delete_dynamic_partition("sources_names_active", s)
    context.log.info(f"new sources {new_sources}")
    context.log.info(f"Removed {removed_sources}")
    return SensorResult(
        run_requests=[
            RunRequest(partition_key=source
                   #    , job_name=f"{source}_load"
            , run_key=f"{source}_load"
                       ) for source in new_sources
        ],
        dynamic_partitions_requests=[
            sources_partitions_def.build_add_request(new_sources)
        ],
    )
#
# https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules#static-partitioned-jobs
# humm https://github.com/dagster-io/dagster/blob/567cb59f1da819bbb8522108fc2c2a3bace6c7b3/python_modules/dagster-test/dagster_test/toys/schedules.py#L41

#     #  so this needs to be a schedule, and we handle the cron by ourselves.)
sched = os.environ.get("GLEANERIO_DEFAULT_SCHEDULE", "@weekly")
sched_timezone = os.environ.get("GLEANERIO_DEFAULT_SCHEDULE_TIMEZONE", "America/Los_Angeles")
@schedule(job=summon_asset_job, cron_schedule=sched,execution_timezone=sched_timezone,
        default_status=DefaultScheduleStatus.RUNNING,
          )
def sources_schedule(context):
    partition_keys = sources_partitions_def.get_partition_keys(dynamic_partitions_store=context.instance)
    get_dagster_logger().info(str(partition_keys))
    return [
        RunRequest(
            partition_key=partition_key,
         #   run_key=f"{context.scheduled_execution_time}_{partition_key}"
          run_key=f"summon_asset_{partition_key}"
        )
        for partition_key in partition_keys
    ]



# from dagster import sensor, RunRequest, SensorExecutionContext
# from dagster import (DynamicPartitionsDefinition, job)
# # Define your dynamic partitions
# fruits = DynamicPartitionsDefinition(name="fruits")
# # Define a job that will process the partitions
# @job()
# def my_job():
#     # Your job logic here
#     pass
# # Define a sensor that triggers the job and updates the partitions
# @sensor(job=my_job)
# def my_sensor(context: SensorExecutionContext):
#     # Logic to determine if there are new partitions to add
#     # For example, check a directory for new files, query a database, etc.
#     new_partitions = ["apple", "banana"]
#     # Replace with your dynamic logic
#     # Build add requests for the new partitions
#     dynamic_partitions_requests = [fruits.build_add_request(new_partitions)]
#     # Create a run request for each new partition
#     run_requests = [RunRequest(partition_key=partition) for partition in new_partitions]
#     # Return the sensor result with run requests and dynamic partition requests
#     return SensorResult(
#         run_requests=run_requests,
#         dynamic_partitions_requests=dynamic_partitions_requests
#     )
