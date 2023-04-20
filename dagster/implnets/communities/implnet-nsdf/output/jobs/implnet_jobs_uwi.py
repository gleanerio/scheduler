from dagster import job

from ops.implnet_ops_uwi import harvest_uwi

@job
def implnet_job_uwi():
    harvest_uwi()