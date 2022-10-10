from dagster import job

from ops.implnet_ops_usgs73 import harvest_usgs73

@job
def implnet_job_usgs73():
    harvest_usgs73()