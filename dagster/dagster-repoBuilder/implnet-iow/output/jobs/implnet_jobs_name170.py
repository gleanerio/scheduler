from dagster import job

from ops.implnet_ops_name170 import harvest_name170

@job
def implnet_job_name170():
    harvest_name170()