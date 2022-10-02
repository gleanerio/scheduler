from dagster import job

from gleaner.ops.oih_euroceanprojects import harvest_euroceanprojects

@job
def oih_job_euroceanprojects():
    harvest_euroceanprojects()