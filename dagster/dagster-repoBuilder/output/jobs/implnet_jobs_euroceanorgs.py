from dagster import job

from gleaner.ops.implnet_euroceanorgs import harvest_euroceanorgs

@job
def implnet_job_euroceanorgs():
    harvest_euroceanorgs()