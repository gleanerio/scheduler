from dagster import job

from ops.implnet_ops_wade6 import harvest_wade6

@job
def implnet_job_wade6():
    harvest_wade6()