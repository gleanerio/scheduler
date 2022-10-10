from dagster import job

from ops.implnet_ops_name181 import harvest_name181

@job
def implnet_job_name181():
    harvest_name181()