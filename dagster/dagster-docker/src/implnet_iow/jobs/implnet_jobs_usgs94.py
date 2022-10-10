from dagster import job

from ops.implnet_ops_usgs94 import harvest_usgs94

@job
def implnet_job_usgs94():
    harvest_usgs94()