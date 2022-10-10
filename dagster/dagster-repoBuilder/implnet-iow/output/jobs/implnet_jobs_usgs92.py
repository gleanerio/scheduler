from dagster import job

from ops.implnet_ops_usgs92 import harvest_usgs92

@job
def implnet_job_usgs92():
    harvest_usgs92()