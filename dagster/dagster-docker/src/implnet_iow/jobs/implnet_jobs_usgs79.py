from dagster import job

from ops.implnet_ops_usgs79 import harvest_usgs79

@job
def implnet_job_usgs79():
    harvest_usgs79()