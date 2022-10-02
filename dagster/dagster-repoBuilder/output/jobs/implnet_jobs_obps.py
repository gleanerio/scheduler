from dagster import job

from gleaner.ops.implnet_obps import harvest_obps

@job
def implnet_job_obps():
    harvest_obps()