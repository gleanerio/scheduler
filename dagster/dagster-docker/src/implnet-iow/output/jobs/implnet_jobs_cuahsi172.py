from dagster import job

from ops.implnet_ops_cuahsi172 import harvest_cuahsi172

@job
def implnet_job_cuahsi172():
    harvest_cuahsi172()