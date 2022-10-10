from dagster import job

from ops.implnet_ops_name131 import harvest_name131

@job
def implnet_job_name131():
    harvest_name131()