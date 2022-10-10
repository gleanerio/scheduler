from dagster import job

from ops.implnet_ops_invemarexpert import harvest_invemarexpert

@job
def implnet_job_invemarexpert():
    harvest_invemarexpert()