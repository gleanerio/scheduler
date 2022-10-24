from dagster import job

from ops.implnet_ops_cuahsi168 import harvest_cuahsi168

@job
def implnet_job_cuahsi168():
    harvest_cuahsi168()