from dagster import job

from ops.implnet_ops_name124 import harvest_name124

@job
def implnet_job_name124():
    harvest_name124()