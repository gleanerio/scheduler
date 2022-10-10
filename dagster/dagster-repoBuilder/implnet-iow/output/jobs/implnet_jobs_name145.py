from dagster import job

from ops.implnet_ops_name145 import harvest_name145

@job
def implnet_job_name145():
    harvest_name145()