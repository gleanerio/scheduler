from dagster import job

from ops.implnet_ops_wade16 import harvest_wade16

@job
def implnet_job_wade16():
    harvest_wade16()