from dagster import job

from ops.implnet_ops_name95 import harvest_name95

@job
def implnet_job_name95():
    harvest_name95()