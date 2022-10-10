from dagster import job

from ops.implnet_ops_name130 import harvest_name130

@job
def implnet_job_name130():
    harvest_name130()