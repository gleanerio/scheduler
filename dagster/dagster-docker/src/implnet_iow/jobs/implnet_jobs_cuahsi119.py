from dagster import job

from ops.implnet_ops_cuahsi119 import harvest_cuahsi119

@job
def implnet_job_cuahsi119():
    harvest_cuahsi119()