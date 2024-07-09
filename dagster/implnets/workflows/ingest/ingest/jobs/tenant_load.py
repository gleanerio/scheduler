from dagster import (
    op, job, Config,
    sensor, RunRequest, RunConfig,
    SensorEvaluationContext, asset_sensor, EventLogEntry,
    SkipReason,
    AssetKey,
    static_partitioned_config, dynamic_partitioned_config, DynamicPartitionsDefinition,
    define_asset_job, AssetSelection,graph_asset,
BackfillPolicy
)

from dagster_aws.s3.sensor import get_s3_keys
from typing import List, Dict
from pydantic import Field

from ..assets import gleanerio_tenants, tenant_partitions_def, sources_partitions_def, upload_release,upload_summary
from ..assets.tenant import create_tenant_containers, create_graph_namespaces
from ..resources.gleanerio import GleanerioResource
from ..resources.gleanerS3 import gleanerS3Resource
from ..resources.graph import BlazegraphResource




tenant_asset_job = define_asset_job(
    name="tenant_config_updated_job",
    selection=AssetSelection.assets(AssetKey(["ingest","tenant_names"])).required_multi_asset_neighbors(),
    partitions_def=sources_partitions_def,
)

release_asset_job = define_asset_job(
    name="tenant_release_job",
    selection=AssetSelection.assets(upload_release,upload_summary),
    partitions_def=sources_partitions_def,
    tags={"dagster/priority": "3"}
 #    tags={"dagster/concurrency_key": 'graph'},
)
#Attempted to set tag with reserved system prefix: dagster/concurrency_key
#File "/usr/local/lib/python3.11/site-packages/dagster/_daemon/sensor.py", line 471, in _process_tick_generator

tenant_namespaces_job = define_asset_job(
    name="tenant_namespaces_job",
    selection=AssetSelection.assets(create_tenant_containers, create_graph_namespaces),
    partitions_def=tenant_partitions_def,
)

# @job(partitions_def=tenant_partitions_def)
# def tenant_namespaces_job(context):
#     source_name = context.asset_partition_key_for_output()
#     context.log.info(f"tenant_name {source_name}")
#     create_tenant_containers(create_graph_namespaces())


class TenantConfig(Config):
    source_name: str
    name: str
    source_list: List[str]
    TENANT_GRAPH_NAMESPACE: str
    TENANT_GRAPH_SUMMARY_NAMESPACE: str
    SUMMARY_PATH: str =  Field(
         description="GLEANERIO_GRAPH_SUMMARY_PATH.", default='graphs/summary')
    RELEASE_PATH : str =  Field(
         description="GLEANERIO_GRAPH_RELEASE_PATH.", default='graphs/latest')
@dynamic_partitioned_config(partition_fn=gleanerio_tenants)
def tenant_config(partition_key: str):

    # default_config ={"ops": {
    #     "upload_release":
    #         {"config":
    #             {
    #                 TenantConfig(
    #                     source_name=partition_key,
    #                     name="name",
    #                     source_list=[],
    #                     TENANT_GRAPH_NAMESPACE="",
    #                     TENANT_GRAPH_SUMMARY_NAMESPACE=""
    #                 )
    #             }
    #             }
    #         },
    #     "upload_summary":
    #         {"config":
    #             {
    #                 TenantConfig(
    #                 source_name=partition_key,
    #                 name="name",
    #                 source_list=[],
    #                 TENANT_GRAPH_NAMESPACE="",
    #                 TENANT_GRAPH_SUMMARY_NAMESPACE=""
    #                 )
    #             }
    #         }
    #     }
    default_config = {"ops": {
        {"upload_release": {"config": {"source_name": partition_key}}},
        {"upload_summary": {"config": {"source_name": partition_key}}}
    }}
    return default_config
