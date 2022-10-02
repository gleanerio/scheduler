from dagster import job

from gleaner.ops.implnet_edmo import harvest_edmo

@job
def implnet_job_edmo():
    harvest_edmo()