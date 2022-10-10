from dagster import job

from ops.implnet_ops_usgs90 import harvest_usgs90

@job
def implnet_job_usgs90():
    harvest_usgs90()