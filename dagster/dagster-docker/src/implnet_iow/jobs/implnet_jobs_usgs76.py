from dagster import job

from ops.implnet_ops_usgs76 import harvest_usgs76

@job
def implnet_job_usgs76():
    harvest_usgs76()