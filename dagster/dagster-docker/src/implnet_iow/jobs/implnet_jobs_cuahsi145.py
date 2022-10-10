from dagster import job

from ops.implnet_ops_cuahsi145 import harvest_cuahsi145

@job
def implnet_job_cuahsi145():
    harvest_cuahsi145()