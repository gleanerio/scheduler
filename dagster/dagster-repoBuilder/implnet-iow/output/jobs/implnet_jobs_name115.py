from dagster import job

from ops.implnet_ops_name115 import harvest_name115

@job
def implnet_job_name115():
    harvest_name115()