from dagster import (
    op, job, Config,
    sensor, RunRequest, RunConfig,
    SensorEvaluationContext, asset_sensor, EventLogEntry,
    SkipReason,
    AssetKey,
    static_partitioned_config, dynamic_partitioned_config, DynamicPartitionsDefinition,
    define_asset_job, AssetSelection, graph_asset,
    BackfillPolicy
)
from ..assets import task_tenant_sources

from dagster_aws.s3.sensor import get_s3_keys
from typing import List, Dict
from pydantic import Field


tenant_asset_job = define_asset_job(
    name="task_tenant_config_updated_job",
    selection=AssetSelection.assets(task_tenant_sources),

)
