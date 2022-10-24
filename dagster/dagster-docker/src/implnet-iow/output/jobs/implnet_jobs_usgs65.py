from dagster import job

from ops.implnet_ops_usgs65 import harvest_usgs65

@job
def implnet_job_usgs65():
    harvest_usgs65()