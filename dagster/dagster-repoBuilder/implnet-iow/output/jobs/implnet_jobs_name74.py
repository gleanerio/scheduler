from dagster import job

from ops.implnet_ops_name74 import harvest_name74

@job
def implnet_job_name74():
    harvest_name74()