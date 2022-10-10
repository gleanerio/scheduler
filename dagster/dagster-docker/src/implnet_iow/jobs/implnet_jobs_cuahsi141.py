from dagster import job

from ops.implnet_ops_cuahsi141 import harvest_cuahsi141

@job
def implnet_job_cuahsi141():
    harvest_cuahsi141()