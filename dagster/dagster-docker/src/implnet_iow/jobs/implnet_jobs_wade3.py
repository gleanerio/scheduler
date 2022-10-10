from dagster import job

from ops.implnet_ops_wade3 import harvest_wade3

@job
def implnet_job_wade3():
    harvest_wade3()