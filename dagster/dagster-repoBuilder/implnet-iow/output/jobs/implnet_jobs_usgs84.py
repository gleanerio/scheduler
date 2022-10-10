from dagster import job

from ops.implnet_ops_usgs84 import harvest_usgs84

@job
def implnet_job_usgs84():
    harvest_usgs84()