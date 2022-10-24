from dagster import job

from ops.implnet_ops_ref46 import harvest_ref46

@job
def implnet_job_ref46():
    harvest_ref46()