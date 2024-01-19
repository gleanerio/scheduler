from dagster import (
    SensorResult, RunRequest,
    EventLogEntry, AssetKey, asset_sensor
)
from ..assets import (
summon_asset_job, sources_partitions_def
)




@asset_sensor( asset_key=AssetKey("gleanerio_orgs"), job=summon_asset_job)
def sources_sensor(context,  asset_event: EventLogEntry):
    assert asset_event.dagster_event and asset_event.dagster_event.asset_key

# well this is a pain. but it works. Cannot just pass it like you do in ops
    # otherwise it's just an AssetDefinition.
    sources = context.repository_def.load_asset_value(AssetKey("gleanerio_orgs"))
    new_sources = [
        source
        for source in sources
        if not sources_partitions_def.has_partition_key(
            source, dynamic_partitions_store=context.instance
        )
    ]

    return SensorResult(
        run_requests=[
            RunRequest(partition_key=source) for source in new_sources
        ],
        dynamic_partitions_requests=[
            sources_partitions_def.build_add_request(new_sources)
        ],
    )
