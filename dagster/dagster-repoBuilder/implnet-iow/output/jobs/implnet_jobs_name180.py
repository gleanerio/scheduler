from dagster import job

from ops.implnet_ops_name180 import harvest_name180

@job
def implnet_job_name180():
    harvest_name180()