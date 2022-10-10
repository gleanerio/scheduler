from dagster import job

from ops.implnet_ops_ref54 import harvest_ref54

@job
def implnet_job_ref54():
    harvest_ref54()