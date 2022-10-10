from dagster import job

from ops.implnet_ops_name35 import harvest_name35

@job
def implnet_job_name35():
    harvest_name35()