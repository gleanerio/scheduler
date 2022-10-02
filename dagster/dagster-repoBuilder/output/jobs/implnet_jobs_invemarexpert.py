from dagster import job

from gleaner.ops.implnet_invemarexpert import harvest_invemarexpert

@job
def implnet_job_invemarexpert():
    harvest_invemarexpert()