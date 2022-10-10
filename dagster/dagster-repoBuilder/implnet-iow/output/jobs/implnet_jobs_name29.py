from dagster import job

from ops.implnet_ops_name29 import harvest_name29

@job
def implnet_job_name29():
    harvest_name29()