from dagster import job

from ops.implnet_ops_name94 import harvest_name94

@job
def implnet_job_name94():
    harvest_name94()