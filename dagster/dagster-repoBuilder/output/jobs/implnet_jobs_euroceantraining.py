from dagster import job

from gleaner.ops.implnet_euroceantraining import harvest_euroceantraining

@job
def implnet_job_euroceantraining():
    harvest_euroceantraining()