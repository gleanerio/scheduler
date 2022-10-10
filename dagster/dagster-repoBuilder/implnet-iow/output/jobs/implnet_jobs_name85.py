from dagster import job

from ops.implnet_ops_name85 import harvest_name85

@job
def implnet_job_name85():
    harvest_name85()