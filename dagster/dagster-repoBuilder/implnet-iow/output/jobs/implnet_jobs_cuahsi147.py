from dagster import job

from ops.implnet_ops_cuahsi147 import harvest_cuahsi147

@job
def implnet_job_cuahsi147():
    harvest_cuahsi147()