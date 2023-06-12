from dagster import job

from ops.implnet_ops_hord import harvest_hord

@job
def implnet_job_hord():
    harvest_hord()