from dagster import job

from ops.implnet_ops_name121 import harvest_name121

@job
def implnet_job_name121():
    harvest_name121()