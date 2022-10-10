from dagster import job

from ops.implnet_ops_cuahsi173 import harvest_cuahsi173

@job
def implnet_job_cuahsi173():
    harvest_cuahsi173()