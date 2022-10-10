from dagster import job

from ops.implnet_ops_cuahsi176 import harvest_cuahsi176

@job
def implnet_job_cuahsi176():
    harvest_cuahsi176()