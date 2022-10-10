from dagster import job

from ops.implnet_ops_name32 import harvest_name32

@job
def implnet_job_name32():
    harvest_name32()