from dagster import job

from ops.implnet_ops_euroceanprojects import harvest_euroceanprojects

@job
def implnet_job_euroceanprojects():
    harvest_euroceanprojects()