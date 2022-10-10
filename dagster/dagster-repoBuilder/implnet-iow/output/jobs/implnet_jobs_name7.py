from dagster import job

from ops.implnet_ops_name7 import harvest_name7

@job
def implnet_job_name7():
    harvest_name7()