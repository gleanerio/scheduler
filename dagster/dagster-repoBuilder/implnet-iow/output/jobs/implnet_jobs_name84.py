from dagster import job

from ops.implnet_ops_name84 import harvest_name84

@job
def implnet_job_name84():
    harvest_name84()