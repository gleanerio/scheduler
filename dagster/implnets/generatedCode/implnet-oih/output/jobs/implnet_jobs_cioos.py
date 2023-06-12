from dagster import job

from ops.implnet_ops_cioos import harvest_cioos

@job
def implnet_job_cioos():
    harvest_cioos()