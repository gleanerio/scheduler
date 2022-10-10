from dagster import job

from ops.implnet_ops_wade4 import harvest_wade4

@job
def implnet_job_wade4():
    harvest_wade4()