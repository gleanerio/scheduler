from dagster import job

from ops.implnet_ops_usgs69 import harvest_usgs69

@job
def implnet_job_usgs69():
    harvest_usgs69()