from dagster import job

from ops.implnet_ops_cuahsi108 import harvest_cuahsi108

@job
def implnet_job_cuahsi108():
    harvest_cuahsi108()