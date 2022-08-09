from dagster import job

from gleaner.ops.oih_obis import harvest_obis

@job
def oih_job_obis():
    harvest_obis()