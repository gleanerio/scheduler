from dagster import job

from ops.implnet_ops_acss import harvest_acss

@job
def implnet_job_acss():
    harvest_acss()