from dagster import job

from ops.implnet_ops_cuahsi181 import harvest_cuahsi181

@job
def implnet_job_cuahsi181():
    harvest_cuahsi181()