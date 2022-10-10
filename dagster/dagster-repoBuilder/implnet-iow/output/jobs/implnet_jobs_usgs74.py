from dagster import job

from ops.implnet_ops_usgs74 import harvest_usgs74

@job
def implnet_job_usgs74():
    harvest_usgs74()