from dagster import job

from gleaner.ops.implnet_euroceanvessels import harvest_euroceanvessels

@job
def implnet_job_euroceanvessels():
    harvest_euroceanvessels()