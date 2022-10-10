from dagster import job

from ops.implnet_ops_name82 import harvest_name82

@job
def implnet_job_name82():
    harvest_name82()