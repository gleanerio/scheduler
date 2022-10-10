from dagster import job

from ops.implnet_ops_name53 import harvest_name53

@job
def implnet_job_name53():
    harvest_name53()