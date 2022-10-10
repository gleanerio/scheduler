from dagster import job

from ops.implnet_ops_usgs88 import harvest_usgs88

@job
def implnet_job_usgs88():
    harvest_usgs88()