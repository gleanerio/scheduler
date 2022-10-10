from dagster import job

from ops.implnet_ops_usgs78 import harvest_usgs78

@job
def implnet_job_usgs78():
    harvest_usgs78()