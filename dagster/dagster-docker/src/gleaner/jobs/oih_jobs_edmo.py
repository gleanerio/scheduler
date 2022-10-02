from dagster import job

from gleaner.ops.oih_edmo import harvest_edmo

@job
def oih_job_edmo():
    harvest_edmo()