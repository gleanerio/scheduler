from dagster import job

from ops.implnet_ops_cuahsi133 import harvest_cuahsi133

@job
def implnet_job_cuahsi133():
    harvest_cuahsi133()