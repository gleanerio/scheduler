from dagster import job

from ops.implnet_ops_usgs96 import harvest_usgs96

@job
def implnet_job_usgs96():
    harvest_usgs96()