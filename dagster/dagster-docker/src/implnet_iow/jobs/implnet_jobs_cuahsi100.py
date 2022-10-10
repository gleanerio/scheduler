from dagster import job

from ops.implnet_ops_cuahsi100 import harvest_cuahsi100

@job
def implnet_job_cuahsi100():
    harvest_cuahsi100()