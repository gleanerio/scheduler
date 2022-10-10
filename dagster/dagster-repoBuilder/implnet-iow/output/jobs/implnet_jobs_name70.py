from dagster import job

from ops.implnet_ops_name70 import harvest_name70

@job
def implnet_job_name70():
    harvest_name70()