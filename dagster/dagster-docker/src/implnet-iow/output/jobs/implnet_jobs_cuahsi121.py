from dagster import job

from ops.implnet_ops_cuahsi121 import harvest_cuahsi121

@job
def implnet_job_cuahsi121():
    harvest_cuahsi121()