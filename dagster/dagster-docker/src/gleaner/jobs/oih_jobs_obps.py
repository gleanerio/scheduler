from dagster import job

from gleaner.ops.oih_obps import harvest_obps

@job
def oih_job_obps():
    harvest_obps()