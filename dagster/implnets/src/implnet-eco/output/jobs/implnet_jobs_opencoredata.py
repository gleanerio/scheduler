from dagster import job

from ops.implnet_ops_opencoredata import harvest_opencoredata

@job
def implnet_job_opencoredata():
    harvest_opencoredata()