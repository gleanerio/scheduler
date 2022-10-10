from dagster import job

from ops.implnet_ops_name152 import harvest_name152

@job
def implnet_job_name152():
    harvest_name152()