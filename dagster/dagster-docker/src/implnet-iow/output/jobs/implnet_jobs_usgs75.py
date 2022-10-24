from dagster import job

from ops.implnet_ops_usgs75 import harvest_usgs75

@job
def implnet_job_usgs75():
    harvest_usgs75()