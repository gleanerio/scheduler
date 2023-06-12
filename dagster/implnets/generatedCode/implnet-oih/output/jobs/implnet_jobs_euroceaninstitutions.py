from dagster import job

from ops.implnet_ops_euroceaninstitutions import harvest_euroceaninstitutions

@job
def implnet_job_euroceaninstitutions():
    harvest_euroceaninstitutions()