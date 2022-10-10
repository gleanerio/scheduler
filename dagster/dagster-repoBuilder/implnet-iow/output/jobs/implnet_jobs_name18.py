from dagster import job

from ops.implnet_ops_name18 import harvest_name18

@job
def implnet_job_name18():
    harvest_name18()