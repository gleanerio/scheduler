from dagster import job

from gleaner.ops.oih_euroceanvessels import harvest_euroceanvessels

@job
def oih_job_euroceanvessels():
    harvest_euroceanvessels()