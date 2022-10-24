from dagster import job

from ops.implnet_ops_usgs87 import harvest_usgs87

@job
def implnet_job_usgs87():
    harvest_usgs87()