from dagster import job

from ops.implnet_ops_cuahsi153 import harvest_cuahsi153

@job
def implnet_job_cuahsi153():
    harvest_cuahsi153()