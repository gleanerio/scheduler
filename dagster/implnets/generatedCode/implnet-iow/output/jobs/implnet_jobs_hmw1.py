from dagster import job

from ops.implnet_ops_hmw1 import harvest_hmw1

@job
def implnet_job_hmw1():
    harvest_hmw1()