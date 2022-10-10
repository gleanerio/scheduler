from dagster import job

from ops.implnet_ops_ref52 import harvest_ref52

@job
def implnet_job_ref52():
    harvest_ref52()