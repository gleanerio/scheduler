from dagster import job

from ops.implnet_ops_usgs71 import harvest_usgs71

@job
def implnet_job_usgs71():
    harvest_usgs71()