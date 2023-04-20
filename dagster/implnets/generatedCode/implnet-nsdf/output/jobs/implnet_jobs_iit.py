from dagster import job

from ops.implnet_ops_iit import harvest_iit

@job
def implnet_job_iit():
    harvest_iit()