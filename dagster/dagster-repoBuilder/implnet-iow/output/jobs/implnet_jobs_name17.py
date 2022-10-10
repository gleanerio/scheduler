from dagster import job

from ops.implnet_ops_name17 import harvest_name17

@job
def implnet_job_name17():
    harvest_name17()