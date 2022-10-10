from dagster import job

from ops.implnet_ops_usgs70 import harvest_usgs70

@job
def implnet_job_usgs70():
    harvest_usgs70()