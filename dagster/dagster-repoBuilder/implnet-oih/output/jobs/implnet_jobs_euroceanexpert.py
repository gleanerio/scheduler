from dagster import job

from ops.implnet_ops_euroceanexpert import harvest_euroceanexpert

@job
def implnet_job_euroceanexpert():
    harvest_euroceanexpert()