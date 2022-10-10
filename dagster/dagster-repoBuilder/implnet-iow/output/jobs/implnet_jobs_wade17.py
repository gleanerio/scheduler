from dagster import job

from ops.implnet_ops_wade17 import harvest_wade17

@job
def implnet_job_wade17():
    harvest_wade17()