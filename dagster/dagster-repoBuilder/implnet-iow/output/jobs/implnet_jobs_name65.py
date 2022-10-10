from dagster import job

from ops.implnet_ops_name65 import harvest_name65

@job
def implnet_job_name65():
    harvest_name65()