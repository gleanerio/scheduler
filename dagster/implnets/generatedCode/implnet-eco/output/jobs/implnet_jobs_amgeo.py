from dagster import job

from ops.implnet_ops_amgeo import harvest_amgeo

@job
def implnet_job_amgeo():
    harvest_amgeo()