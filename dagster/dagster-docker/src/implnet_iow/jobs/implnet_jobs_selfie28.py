from dagster import job

from ops.implnet_ops_selfie28 import harvest_selfie28

@job
def implnet_job_selfie28():
    harvest_selfie28()