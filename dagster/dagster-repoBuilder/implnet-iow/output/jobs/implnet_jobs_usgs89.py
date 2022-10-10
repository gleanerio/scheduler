from dagster import job

from ops.implnet_ops_usgs89 import harvest_usgs89

@job
def implnet_job_usgs89():
    harvest_usgs89()