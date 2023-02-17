from dagster import job

from ops.implnet_ops_wade1 import harvest_wade1

@job
def implnet_job_wade1():
    harvest_wade1()