from dagster import job

from ops.implnet_ops_name61 import harvest_name61

@job
def implnet_job_name61():
    harvest_name61()