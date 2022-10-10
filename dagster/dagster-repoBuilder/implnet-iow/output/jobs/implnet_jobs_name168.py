from dagster import job

from ops.implnet_ops_name168 import harvest_name168

@job
def implnet_job_name168():
    harvest_name168()