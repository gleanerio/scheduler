from dagster import job

from ops.implnet_ops_name31 import harvest_name31

@job
def implnet_job_name31():
    harvest_name31()