from dagster import job

from ops.implnet_ops_name75 import harvest_name75

@job
def implnet_job_name75():
    harvest_name75()