from dagster import job

from ops.implnet_ops_name166 import harvest_name166

@job
def implnet_job_name166():
    harvest_name166()