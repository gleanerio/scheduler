from dagster import job

from gleaner.ops.implnet_SOURCEVAL import harvest_SOURCEVAL

@job
def implnet_job_SOURCEVAL():
    harvest_SOURCEVAL()