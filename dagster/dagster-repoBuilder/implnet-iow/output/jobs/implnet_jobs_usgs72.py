from dagster import job

from ops.implnet_ops_usgs72 import harvest_usgs72

@job
def implnet_job_usgs72():
    harvest_usgs72()