from dagster import job

from ops.implnet_ops_name88 import harvest_name88

@job
def implnet_job_name88():
    harvest_name88()