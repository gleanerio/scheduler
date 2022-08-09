from dagster import job

from gleaner.ops.oih_invemarexpert import harvest_invemarexpert

@job
def oih_job_invemarexpert():
    harvest_invemarexpert()