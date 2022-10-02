from dagster import job

from gleaner.ops.oih_euroceanexpert import harvest_euroceanexpert

@job
def oih_job_euroceanexpert():
    harvest_euroceanexpert()