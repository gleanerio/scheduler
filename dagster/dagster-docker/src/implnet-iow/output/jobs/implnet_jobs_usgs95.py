from dagster import job

from ops.implnet_ops_usgs95 import harvest_usgs95

@job
def implnet_job_usgs95():
    harvest_usgs95()