from dagster import job

from ops.implnet_ops_wade2 import harvest_wade2

@job
def implnet_job_wade2():
    harvest_wade2()