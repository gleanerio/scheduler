from dagster import job

from ops.implnet_ops_name175 import harvest_name175

@job
def implnet_job_name175():
    harvest_name175()