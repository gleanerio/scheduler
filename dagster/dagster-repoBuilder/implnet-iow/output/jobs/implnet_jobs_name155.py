from dagster import job

from ops.implnet_ops_name155 import harvest_name155

@job
def implnet_job_name155():
    harvest_name155()