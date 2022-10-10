from dagster import job

from ops.implnet_ops_name172 import harvest_name172

@job
def implnet_job_name172():
    harvest_name172()