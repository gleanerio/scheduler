from dagster import job

from ops.implnet_ops_name83 import harvest_name83

@job
def implnet_job_name83():
    harvest_name83()