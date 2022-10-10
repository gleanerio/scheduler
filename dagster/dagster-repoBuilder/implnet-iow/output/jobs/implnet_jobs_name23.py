from dagster import job

from ops.implnet_ops_name23 import harvest_name23

@job
def implnet_job_name23():
    harvest_name23()