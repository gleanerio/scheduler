from dagster import job

from ops.implnet_ops_cuahsi104 import harvest_cuahsi104

@job
def implnet_job_cuahsi104():
    harvest_cuahsi104()