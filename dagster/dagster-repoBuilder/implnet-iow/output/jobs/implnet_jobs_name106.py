from dagster import job

from ops.implnet_ops_name106 import harvest_name106

@job
def implnet_job_name106():
    harvest_name106()