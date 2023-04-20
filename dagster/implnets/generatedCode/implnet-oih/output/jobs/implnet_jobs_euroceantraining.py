from dagster import job

from ops.implnet_ops_euroceantraining import harvest_euroceantraining

@job
def implnet_job_euroceantraining():
    harvest_euroceantraining()