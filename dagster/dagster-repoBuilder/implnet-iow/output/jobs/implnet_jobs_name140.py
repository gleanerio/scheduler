from dagster import job

from ops.implnet_ops_name140 import harvest_name140

@job
def implnet_job_name140():
    harvest_name140()