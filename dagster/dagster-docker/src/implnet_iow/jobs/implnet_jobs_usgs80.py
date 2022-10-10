from dagster import job

from ops.implnet_ops_usgs80 import harvest_usgs80

@job
def implnet_job_usgs80():
    harvest_usgs80()