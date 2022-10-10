from dagster import job

from ops.implnet_ops_name119 import harvest_name119

@job
def implnet_job_name119():
    harvest_name119()