from dagster import job

from ops.implnet_ops_ref58 import harvest_ref58

@job
def implnet_job_ref58():
    harvest_ref58()