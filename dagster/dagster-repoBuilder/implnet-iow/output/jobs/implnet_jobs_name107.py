from dagster import job

from ops.implnet_ops_name107 import harvest_name107

@job
def implnet_job_name107():
    harvest_name107()