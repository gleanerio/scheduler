from dagster import job

from ops.implnet_ops_lipdverse import harvest_lipdverse

@job
def implnet_job_lipdverse():
    harvest_lipdverse()