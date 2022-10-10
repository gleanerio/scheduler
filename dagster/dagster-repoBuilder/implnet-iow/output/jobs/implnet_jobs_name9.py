from dagster import job

from ops.implnet_ops_name9 import harvest_name9

@job
def implnet_job_name9():
    harvest_name9()