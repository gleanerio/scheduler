from dagster import job

from ops.implnet_ops_ref53 import harvest_ref53

@job
def implnet_job_ref53():
    harvest_ref53()