from dagster import job

from gleaner.ops.implnet_obis import harvest_obis

@job
def implnet_job_obis():
    harvest_obis()