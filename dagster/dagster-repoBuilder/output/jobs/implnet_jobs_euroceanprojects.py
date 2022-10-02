from dagster import job

from gleaner.ops.implnet_euroceanprojects import harvest_euroceanprojects

@job
def implnet_job_euroceanprojects():
    harvest_euroceanprojects()