from dagster import job

from ops.implnet_ops_name96 import harvest_name96

@job
def implnet_job_name96():
    harvest_name96()