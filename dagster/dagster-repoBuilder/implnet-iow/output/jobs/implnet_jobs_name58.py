from dagster import job

from ops.implnet_ops_name58 import harvest_name58

@job
def implnet_job_name58():
    harvest_name58()