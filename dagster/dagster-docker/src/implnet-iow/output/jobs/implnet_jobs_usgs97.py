from dagster import job

from ops.implnet_ops_usgs97 import harvest_usgs97

@job
def implnet_job_usgs97():
    harvest_usgs97()