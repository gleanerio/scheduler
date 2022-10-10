from dagster import job

from ops.implnet_ops_cuahsi170 import harvest_cuahsi170

@job
def implnet_job_cuahsi170():
    harvest_cuahsi170()