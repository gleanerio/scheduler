from dagster import job

from gleaner.ops.oih_oceanexperts import harvest_oceanexperts

@job
def oih_job_oceanexperts():
    harvest_oceanexperts()