from dagster import job

from ops.implnet_ops_cuahsi158 import harvest_cuahsi158

@job
def implnet_job_cuahsi158():
    harvest_cuahsi158()