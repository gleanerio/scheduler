from dagster import job

from ops.implnet_ops_usgs64 import harvest_usgs64

@job
def implnet_job_usgs64():
    harvest_usgs64()