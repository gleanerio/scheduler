from dagster import job

from ops.implnet_ops_name15 import harvest_name15

@job
def implnet_job_name15():
    harvest_name15()