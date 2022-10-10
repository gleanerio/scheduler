from dagster import job

from ops.implnet_ops_cuahsi159 import harvest_cuahsi159

@job
def implnet_job_cuahsi159():
    harvest_cuahsi159()