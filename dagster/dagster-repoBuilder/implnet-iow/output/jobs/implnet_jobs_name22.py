from dagster import job

from ops.implnet_ops_name22 import harvest_name22

@job
def implnet_job_name22():
    harvest_name22()