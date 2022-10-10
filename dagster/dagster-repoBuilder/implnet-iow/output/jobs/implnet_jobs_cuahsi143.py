from dagster import job

from ops.implnet_ops_cuahsi143 import harvest_cuahsi143

@job
def implnet_job_cuahsi143():
    harvest_cuahsi143()