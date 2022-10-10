from dagster import job

from ops.implnet_ops_name160 import harvest_name160

@job
def implnet_job_name160():
    harvest_name160()