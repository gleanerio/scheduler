from dagster import job

from ops.implnet_ops_ref44 import harvest_ref44

@job
def implnet_job_ref44():
    harvest_ref44()