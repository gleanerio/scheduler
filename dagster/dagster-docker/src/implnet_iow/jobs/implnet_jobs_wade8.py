from dagster import job

from ops.implnet_ops_wade8 import harvest_wade8

@job
def implnet_job_wade8():
    harvest_wade8()