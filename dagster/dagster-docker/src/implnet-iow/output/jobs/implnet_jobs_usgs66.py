from dagster import job

from ops.implnet_ops_usgs66 import harvest_usgs66

@job
def implnet_job_usgs66():
    harvest_usgs66()