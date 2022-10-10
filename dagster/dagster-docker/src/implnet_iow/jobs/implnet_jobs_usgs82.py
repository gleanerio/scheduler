from dagster import job

from ops.implnet_ops_usgs82 import harvest_usgs82

@job
def implnet_job_usgs82():
    harvest_usgs82()