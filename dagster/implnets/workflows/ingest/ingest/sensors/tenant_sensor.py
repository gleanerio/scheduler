from dagster import (
op, job, Config,get_dagster_logger,
sensor, RunRequest, RunConfig,SensorResult,
SensorEvaluationContext,asset_sensor, EventLogEntry,
SkipReason,
AssetKey,
static_partitioned_config,DynamicPartitionsDefinition,
DefaultSensorStatus,DefaultScheduleStatus
)
from ..jobs.tenant_load import tenant_namespaces_job, release_asset_job
from ..assets import tenant_partitions_def
#from ..assets.tenant import build_community

## Thinking. Doing this the wrong way.
##   for each source, we dynamically generate a set of tenants to load, rather than for each tenant we reload
##  So, at the end of a source load, we trigger a load tenants.
##   this figures out what tenants to load, and call those ops.

## So the asset key is not tenant names, it is still source_names_active.

# now we do need to build tenants when a new tenant is added.
# this should just handle the cretion of namespaces, and adding the UI's

@asset_sensor( asset_key=AssetKey(["ingest","tenant_names"]),
               default_status=DefaultSensorStatus.RUNNING,
#default_status=DefaultScheduleStatus.RUNNING,
               job=tenant_namespaces_job,
         #      jobs=[tenant_namespaces_job,release_asset_job]
   # , minimum_interval_seconds=600
               )
def tenant_names_sensor(context,  asset_event: EventLogEntry):
    context.log.info(f"tenant_names_sensor: start")
    assert asset_event.dagster_event and asset_event.dagster_event.asset_key
    context.log.info(f"asset_key: {asset_event.dagster_event.asset_key}")
# well this is a pain. but it works. Cannot just pass it like you do in ops
    # otherwise it's just an AssetDefinition.
    tenants = context.repository_def.load_asset_value(AssetKey(["ingest","tenant_names"]))
    new_tenants = [
        tenant
        for tenant in tenants
        if not tenant_partitions_def.has_partition_key(
            tenant, dynamic_partitions_store=context.instance
        )
    ]
    removed_tenants  = [
        tenant
        for tenant  in tenant_partitions_def.get_partition_keys(dynamic_partitions_store=context.instance)
        if not tenant in tenants
    ]
    for t in removed_tenants:
        context.instance.delete_dynamic_partition("tenant_names_paritition", t)
    context.log.info(f"Removed {removed_tenants}")
    context.log.info(f"new tenant {new_tenants}")
    return SensorResult(
        run_requests=[
            RunRequest(partition_key=tenant
                   #    , job_name=f"{source}_load"
            , run_key=f"{tenant}_tenant"
                       ) for tenant in new_tenants
        ],
        dynamic_partitions_requests=[
            tenant_partitions_def.build_add_request(new_tenants)
        ],
    )

@asset_sensor( asset_key=AssetKey(["ingest","tenant_names"]),
               default_status=DefaultSensorStatus.RUNNING,
#default_status=DefaultScheduleStatus.RUNNING,
         #      job=tenant_namespaces_job,
               jobs=[tenant_namespaces_job,release_asset_job]
   # , minimum_interval_seconds=600
               )
def tenant_names_sensor_v2(context,  asset_event: EventLogEntry):
    assert asset_event.dagster_event and asset_event.dagster_event.asset_key

# well this is a pain. but it works. Cannot just pass it like you do in ops
    # otherwise it's just an AssetDefinition.
    tenants = context.repository_def.load_asset_value(AssetKey(["ingest","tenant_names"]))
    new_tenants = [
        tenant
        for tenant in tenants
        if not tenant_partitions_def.has_partition_key(
            tenant, dynamic_partitions_store=context.instance
        )
    ]
# in order for this to work, the tenant_release_job  needs to be fed valid sources,
# from some aggreate from the sources in the new_tenants[*]['sources']

    return SensorResult(
        run_requests=[
            RunRequest(partition_key=tenant
                       , job_name="tenant_namespaces_job"
            , run_key=f"{tenant}_tenant_namespace"
                       ) for tenant in new_tenants
        ] + [
            RunRequest(partition_key=tenant
                       , job_name="tenant_release_job"
            , run_key=f"{tenant}_tenant_release"
                       ) for tenant in new_tenants
        ],
        dynamic_partitions_requests=[
            tenant_partitions_def.build_add_request(new_tenants)
        ],
    )
