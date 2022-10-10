from dagster import job

from ops.implnet_ops_name111 import harvest_name111

@job
def implnet_job_name111():
    harvest_name111()