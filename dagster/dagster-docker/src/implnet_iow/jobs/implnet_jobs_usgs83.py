from dagster import job

from ops.implnet_ops_usgs83 import harvest_usgs83

@job
def implnet_job_usgs83():
    harvest_usgs83()