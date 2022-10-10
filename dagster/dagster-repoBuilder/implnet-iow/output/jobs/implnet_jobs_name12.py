from dagster import job

from ops.implnet_ops_name12 import harvest_name12

@job
def implnet_job_name12():
    harvest_name12()