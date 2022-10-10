from dagster import job

from ops.implnet_ops_usgs93 import harvest_usgs93

@job
def implnet_job_usgs93():
    harvest_usgs93()