from dagster import job

from ops.implnet_ops_wade12 import harvest_wade12

@job
def implnet_job_wade12():
    harvest_wade12()