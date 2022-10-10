from dagster import job

from ops.implnet_ops_name20 import harvest_name20

@job
def implnet_job_name20():
    harvest_name20()