from dagster import job

from ops.implnet_ops_cuahsi110 import harvest_cuahsi110

@job
def implnet_job_cuahsi110():
    harvest_cuahsi110()