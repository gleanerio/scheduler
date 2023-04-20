from dagster import job

from ops.implnet_ops_hopkins import harvest_hopkins

@job
def implnet_job_hopkins():
    harvest_hopkins()