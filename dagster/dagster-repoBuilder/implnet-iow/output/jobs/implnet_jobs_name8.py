from dagster import job

from ops.implnet_ops_name8 import harvest_name8

@job
def implnet_job_name8():
    harvest_name8()