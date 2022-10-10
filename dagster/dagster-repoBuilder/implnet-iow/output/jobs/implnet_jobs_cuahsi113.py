from dagster import job

from ops.implnet_ops_cuahsi113 import harvest_cuahsi113

@job
def implnet_job_cuahsi113():
    harvest_cuahsi113()