from dagster import job

from gleaner.ops.implnet_euroceanexpert import harvest_euroceanexpert

@job
def implnet_job_euroceanexpert():
    harvest_euroceanexpert()