from dagster import job

from ops.implnet_ops_name68 import harvest_name68

@job
def implnet_job_name68():
    harvest_name68()