from dagster import job

from ops.implnet_ops_name3 import harvest_name3

@job
def implnet_job_name3():
    harvest_name3()