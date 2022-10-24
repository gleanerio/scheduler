from dagster import job

from ops.implnet_ops_resource_registry import harvest_resource_registry

@job
def implnet_job_resource_registry():
    harvest_resource_registry()