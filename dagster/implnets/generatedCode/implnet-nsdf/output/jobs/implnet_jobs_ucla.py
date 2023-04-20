from dagster import job

from ops.implnet_ops_ucla import harvest_ucla

@job
def implnet_job_ucla():
    harvest_ucla()