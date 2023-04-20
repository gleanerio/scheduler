from dagster import job

from ops.implnet_ops_wardr import harvest_wardr

@job
def implnet_job_wardr():
    harvest_wardr()