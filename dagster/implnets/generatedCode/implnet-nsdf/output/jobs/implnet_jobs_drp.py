from dagster import job

from ops.implnet_ops_drp import harvest_drp

@job
def implnet_job_drp():
    harvest_drp()