from dagster import job

from ops.implnet_ops_cuahsi150 import harvest_cuahsi150

@job
def implnet_job_cuahsi150():
    harvest_cuahsi150()