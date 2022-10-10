from dagster import job

from ops.implnet_ops_name122 import harvest_name122

@job
def implnet_job_name122():
    harvest_name122()