from dagster import job

from ops.implnet_ops_name77 import harvest_name77

@job
def implnet_job_name77():
    harvest_name77()