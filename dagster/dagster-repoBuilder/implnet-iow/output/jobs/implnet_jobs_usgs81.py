from dagster import job

from ops.implnet_ops_usgs81 import harvest_usgs81

@job
def implnet_job_usgs81():
    harvest_usgs81()