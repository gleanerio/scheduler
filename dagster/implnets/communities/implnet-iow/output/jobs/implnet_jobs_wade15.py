from dagster import job

from ops.implnet_ops_wade15 import harvest_wade15

@job
def implnet_job_wade15():
    harvest_wade15()