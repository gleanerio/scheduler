from dagster import job

from ops.implnet_ops_ssdbiodp import harvest_ssdbiodp

@job
def implnet_job_ssdbiodp():
    harvest_ssdbiodp()