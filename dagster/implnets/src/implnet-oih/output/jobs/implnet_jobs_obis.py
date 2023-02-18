from dagster import job

from ops.implnet_ops_obis import harvest_obis

@job
def implnet_job_obis():
    harvest_obis()