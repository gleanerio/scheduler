from dagster import job

from ops.implnet_ops_ua100 import harvest_ua100

@job
def implnet_job_ua100():
    harvest_ua100()