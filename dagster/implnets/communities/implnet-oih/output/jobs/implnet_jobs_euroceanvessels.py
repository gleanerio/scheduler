from dagster import job

from ops.implnet_ops_euroceanvessels import harvest_euroceanvessels

@job
def implnet_job_euroceanvessels():
    harvest_euroceanvessels()