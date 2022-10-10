from dagster import job

from ops.implnet_ops_name135 import harvest_name135

@job
def implnet_job_name135():
    harvest_name135()