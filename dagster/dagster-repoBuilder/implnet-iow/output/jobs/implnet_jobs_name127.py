from dagster import job

from ops.implnet_ops_name127 import harvest_name127

@job
def implnet_job_name127():
    harvest_name127()