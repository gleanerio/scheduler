from dagster import job

from ops.implnet_ops_name109 import harvest_name109

@job
def implnet_job_name109():
    harvest_name109()