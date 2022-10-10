from dagster import job

from ops.implnet_ops_cuahsi175 import harvest_cuahsi175

@job
def implnet_job_cuahsi175():
    harvest_cuahsi175()