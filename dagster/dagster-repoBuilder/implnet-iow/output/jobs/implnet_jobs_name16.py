from dagster import job

from ops.implnet_ops_name16 import harvest_name16

@job
def implnet_job_name16():
    harvest_name16()