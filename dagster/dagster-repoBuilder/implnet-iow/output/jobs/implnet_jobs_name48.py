from dagster import job

from ops.implnet_ops_name48 import harvest_name48

@job
def implnet_job_name48():
    harvest_name48()