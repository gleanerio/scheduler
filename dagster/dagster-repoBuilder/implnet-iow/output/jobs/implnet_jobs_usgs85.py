from dagster import job

from ops.implnet_ops_usgs85 import harvest_usgs85

@job
def implnet_job_usgs85():
    harvest_usgs85()