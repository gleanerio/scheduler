from dagster import job

from ops.implnet_ops_name110 import harvest_name110

@job
def implnet_job_name110():
    harvest_name110()