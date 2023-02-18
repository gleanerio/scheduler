from dagster import job

from ops.implnet_ops_invemarvessels import harvest_invemarvessels

@job
def implnet_job_invemarvessels():
    harvest_invemarvessels()