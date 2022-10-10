from dagster import job

from ops.implnet_ops_cuahsi106 import harvest_cuahsi106

@job
def implnet_job_cuahsi106():
    harvest_cuahsi106()