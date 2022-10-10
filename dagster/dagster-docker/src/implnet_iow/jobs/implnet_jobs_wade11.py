from dagster import job

from ops.implnet_ops_wade11 import harvest_wade11

@job
def implnet_job_wade11():
    harvest_wade11()