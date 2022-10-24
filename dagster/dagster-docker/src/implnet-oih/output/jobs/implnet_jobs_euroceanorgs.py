from dagster import job

from ops.implnet_ops_euroceanorgs import harvest_euroceanorgs

@job
def implnet_job_euroceanorgs():
    harvest_euroceanorgs()