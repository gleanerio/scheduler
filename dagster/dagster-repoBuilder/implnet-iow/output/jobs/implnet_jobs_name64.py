from dagster import job

from ops.implnet_ops_name64 import harvest_name64

@job
def implnet_job_name64():
    harvest_name64()