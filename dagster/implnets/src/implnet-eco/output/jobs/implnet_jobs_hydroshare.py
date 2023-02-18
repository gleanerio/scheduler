from dagster import job

from ops.implnet_ops_hydroshare import harvest_hydroshare

@job
def implnet_job_hydroshare():
    harvest_hydroshare()