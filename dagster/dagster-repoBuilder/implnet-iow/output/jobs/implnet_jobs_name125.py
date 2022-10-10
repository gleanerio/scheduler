from dagster import job

from ops.implnet_ops_name125 import harvest_name125

@job
def implnet_job_name125():
    harvest_name125()