from dagster import job

from ops.implnet_ops_hmw0 import harvest_hmw0

@job
def implnet_job_hmw0():
    harvest_hmw0()