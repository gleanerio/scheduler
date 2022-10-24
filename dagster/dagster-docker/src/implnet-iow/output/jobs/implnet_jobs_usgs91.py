from dagster import job

from ops.implnet_ops_usgs91 import harvest_usgs91

@job
def implnet_job_usgs91():
    harvest_usgs91()