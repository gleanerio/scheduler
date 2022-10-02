from dagster import job

from gleaner.ops.oih_euroceanorgs import harvest_euroceanorgs

@job
def oih_job_euroceanorgs():
    harvest_euroceanorgs()