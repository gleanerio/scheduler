from dagster import job

from ops.implnet_ops_cuahsi149 import harvest_cuahsi149

@job
def implnet_job_cuahsi149():
    harvest_cuahsi149()