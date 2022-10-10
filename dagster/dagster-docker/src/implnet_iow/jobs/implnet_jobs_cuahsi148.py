from dagster import job

from ops.implnet_ops_cuahsi148 import harvest_cuahsi148

@job
def implnet_job_cuahsi148():
    harvest_cuahsi148()