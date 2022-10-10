from dagster import job

from ops.implnet_ops_name100 import harvest_name100

@job
def implnet_job_name100():
    harvest_name100()