from dagster import job

from ops.implnet_ops_cuahsi103 import harvest_cuahsi103

@job
def implnet_job_cuahsi103():
    harvest_cuahsi103()