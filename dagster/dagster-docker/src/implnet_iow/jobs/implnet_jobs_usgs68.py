from dagster import job

from ops.implnet_ops_usgs68 import harvest_usgs68

@job
def implnet_job_usgs68():
    harvest_usgs68()