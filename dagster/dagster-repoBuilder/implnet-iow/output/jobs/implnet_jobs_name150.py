from dagster import job

from ops.implnet_ops_name150 import harvest_name150

@job
def implnet_job_name150():
    harvest_name150()