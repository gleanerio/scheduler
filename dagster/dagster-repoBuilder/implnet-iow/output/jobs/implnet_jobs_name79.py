from dagster import job

from ops.implnet_ops_name79 import harvest_name79

@job
def implnet_job_name79():
    harvest_name79()