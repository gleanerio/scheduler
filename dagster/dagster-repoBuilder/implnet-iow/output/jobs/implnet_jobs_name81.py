from dagster import job

from ops.implnet_ops_name81 import harvest_name81

@job
def implnet_job_name81():
    harvest_name81()