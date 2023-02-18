from dagster import job

from ops.implnet_ops_r2r import harvest_r2r

@job
def implnet_job_r2r():
    harvest_r2r()