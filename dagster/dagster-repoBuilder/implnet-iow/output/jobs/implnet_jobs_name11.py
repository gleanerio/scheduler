from dagster import job

from ops.implnet_ops_name11 import harvest_name11

@job
def implnet_job_name11():
    harvest_name11()