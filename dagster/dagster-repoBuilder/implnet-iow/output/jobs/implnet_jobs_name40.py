from dagster import job

from ops.implnet_ops_name40 import harvest_name40

@job
def implnet_job_name40():
    harvest_name40()