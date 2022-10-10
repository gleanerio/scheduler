from dagster import job

from ops.implnet_ops_name27 import harvest_name27

@job
def implnet_job_name27():
    harvest_name27()