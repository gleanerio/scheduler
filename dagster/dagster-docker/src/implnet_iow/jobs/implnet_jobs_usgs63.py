from dagster import job

from ops.implnet_ops_usgs63 import harvest_usgs63

@job
def implnet_job_usgs63():
    harvest_usgs63()