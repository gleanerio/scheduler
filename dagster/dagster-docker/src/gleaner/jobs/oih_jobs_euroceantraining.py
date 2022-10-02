from dagster import job

from gleaner.ops.oih_euroceantraining import harvest_euroceantraining

@job
def oih_job_euroceantraining():
    harvest_euroceantraining()