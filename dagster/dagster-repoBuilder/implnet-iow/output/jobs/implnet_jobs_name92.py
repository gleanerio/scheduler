from dagster import job

from ops.implnet_ops_name92 import harvest_name92

@job
def implnet_job_name92():
    harvest_name92()