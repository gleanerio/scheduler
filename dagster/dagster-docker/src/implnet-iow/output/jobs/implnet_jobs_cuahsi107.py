from dagster import job

from ops.implnet_ops_cuahsi107 import harvest_cuahsi107

@job
def implnet_job_cuahsi107():
    harvest_cuahsi107()