from dagster import job

from ops.implnet_ops_cuahsi155 import harvest_cuahsi155

@job
def implnet_job_cuahsi155():
    harvest_cuahsi155()