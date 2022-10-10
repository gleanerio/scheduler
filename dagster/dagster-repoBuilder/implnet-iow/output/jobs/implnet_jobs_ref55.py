from dagster import job

from ops.implnet_ops_ref55 import harvest_ref55

@job
def implnet_job_ref55():
    harvest_ref55()