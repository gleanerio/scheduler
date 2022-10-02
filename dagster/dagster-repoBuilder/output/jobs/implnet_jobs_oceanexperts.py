from dagster import job

from gleaner.ops.implnet_oceanexperts import harvest_oceanexperts

@job
def implnet_job_oceanexperts():
    harvest_oceanexperts()