from dagster import job

from ops.implnet_ops_wade19 import harvest_wade19

@job
def implnet_job_wade19():
    harvest_wade19()