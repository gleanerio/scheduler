from dagster import job

from ops.implnet_ops_name6 import harvest_name6

@job
def implnet_job_name6():
    harvest_name6()