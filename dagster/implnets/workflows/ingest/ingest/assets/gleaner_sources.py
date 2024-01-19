# a test asset to see that all the resource configurations load.
# basically runs the first step, of gleaner on geocodes demo datasets
import orjson

import dagster
from dagster import get_dagster_logger, asset, In, Nothing, Config,DynamicPartitionsDefinition, sensor

sources_partitions_def = DynamicPartitionsDefinition(name="gleanerio_orgs")
from ..resources.gleanerio import GleanerioResource

### PRESENT HACK. Using the orgs
# really needs to read a future tenant file, and then add
# new partions with a sensor
# need to add a sensor to add paritions when one is added
# https://docs.dagster.io/concepts/partitions-schedules-sensors/partitioning-assets#dynamically-partitioned-assets

# for right now, using a list of orgs as the sources.
# future read the gleaner config file.
# future future, store soruces and read them.


@asset(required_resource_keys={"gs3"})
def gleanerio_orgs(context ):
    s3_resource = context.resources.gs3
    source="geocodes_demo_datasets"
    files = s3_resource.listPath(path='orgs')
    orgs = list(map(lambda o: o["Key"].removeprefix("orgs/").removesuffix(".nq") , files))
    dagster.get_dagster_logger().info(str(orgs))
    context.add_output_metadata(
            metadata={
                "source": source,  # Metadata can be any key-value pair
                "run": "gleaner",
                # The `MetadataValue` class has useful static methods to build Metadata
            }
        )
    #return orjson.dumps(orgs,  option=orjson.OPT_INDENT_2)
    # this is used for partitioning, so let it pickle (aka be a python list)
    return orgs

# @asset(required_resource_keys={"gs3"})
# def gleanerio_orgs(context ):
#     s3_resource = context.resources.gs3
#     source="geocodes_demo_datasets"
#     files = s3_resource.listPath(path='orgs')
#     orgs = list(map(lambda o: o["Key"].removeprefix("orgs/").removesuffix(".nq") , files))
#     # rather than do this with an @asset_sensor, just do it here.
#     sources = orgs
#     new_sources = [
#         source
#         for source in sources
#         if not sources_partitions_def.has_partition_key(
#             source, dynamic_partitions_store=context.instance
#         )
#     ]
#     sources_partitions_def.build_add_request(new_sources)
#     # return SensorResult(
#     #     run_requests=[
#     #         RunRequest(partition_key=source) for source in new_sources
#     #     ],
#     #     dynamic_partitions_requests=[
#     #         sources_partitions_def.build_add_request(new_sources)
#     #     ],
#     # )
#     dagster.get_dagster_logger().info(str(orgs))
#     context.add_output_metadata(
#             metadata={
#                 "source": source,  # Metadata can be any key-value pair
#                 "new_sources":new_sources,
#                 "run": "gleaner",
#                 # The `MetadataValue` class has useful static methods to build Metadata
#             }
#         )
#     #return orjson.dumps(orgs,  option=orjson.OPT_INDENT_2)
#     # this is used for partitioning, so let it pickle (aka be a python list)
#     return orgs
