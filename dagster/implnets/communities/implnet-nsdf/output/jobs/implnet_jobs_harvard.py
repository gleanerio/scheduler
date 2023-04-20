from dagster import job

from ops.implnet_ops_harvard import harvest_harvard

@job
def implnet_job_harvard():
    harvest_harvard()