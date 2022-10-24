from dagster import job

from ops.implnet_ops_usgs77 import harvest_usgs77

@job
def implnet_job_usgs77():
    harvest_usgs77()