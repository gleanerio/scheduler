from dagster import job

from ops.implnet_ops_name72 import harvest_name72

@job
def implnet_job_name72():
    harvest_name72()