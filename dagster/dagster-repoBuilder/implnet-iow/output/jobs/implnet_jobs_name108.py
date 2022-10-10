from dagster import job

from ops.implnet_ops_name108 import harvest_name108

@job
def implnet_job_name108():
    harvest_name108()