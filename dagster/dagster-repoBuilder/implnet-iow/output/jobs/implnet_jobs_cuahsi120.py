from dagster import job

from ops.implnet_ops_cuahsi120 import harvest_cuahsi120

@job
def implnet_job_cuahsi120():
    harvest_cuahsi120()