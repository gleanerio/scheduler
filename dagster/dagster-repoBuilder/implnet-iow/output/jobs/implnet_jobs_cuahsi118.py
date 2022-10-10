from dagster import job

from ops.implnet_ops_cuahsi118 import harvest_cuahsi118

@job
def implnet_job_cuahsi118():
    harvest_cuahsi118()