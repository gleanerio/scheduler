from dagster import job

from ops.implnet_ops_name4 import harvest_name4

@job
def implnet_job_name4():
    harvest_name4()