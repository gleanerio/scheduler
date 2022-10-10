from dagster import job

from ops.implnet_ops_usgs62 import harvest_usgs62

@job
def implnet_job_usgs62():
    harvest_usgs62()