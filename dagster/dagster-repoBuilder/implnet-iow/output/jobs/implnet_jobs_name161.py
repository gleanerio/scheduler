from dagster import job

from ops.implnet_ops_name161 import harvest_name161

@job
def implnet_job_name161():
    harvest_name161()