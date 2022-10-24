from dagster import job

from ops.implnet_ops_cuahsi140 import harvest_cuahsi140

@job
def implnet_job_cuahsi140():
    harvest_cuahsi140()