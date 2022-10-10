from dagster import job

from ops.implnet_ops_name36 import harvest_name36

@job
def implnet_job_name36():
    harvest_name36()