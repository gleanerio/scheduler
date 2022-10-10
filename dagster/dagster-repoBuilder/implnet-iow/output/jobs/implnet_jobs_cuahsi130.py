from dagster import job

from ops.implnet_ops_cuahsi130 import harvest_cuahsi130

@job
def implnet_job_cuahsi130():
    harvest_cuahsi130()