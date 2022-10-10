from dagster import job

from ops.implnet_ops_cuahsi134 import harvest_cuahsi134

@job
def implnet_job_cuahsi134():
    harvest_cuahsi134()