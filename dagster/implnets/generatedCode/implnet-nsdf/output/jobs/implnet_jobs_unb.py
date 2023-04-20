from dagster import job

from ops.implnet_ops_unb import harvest_unb

@job
def implnet_job_unb():
    harvest_unb()