from dagster import job

from ops.implnet_ops_marinetraining import harvest_marinetraining

@job
def implnet_job_marinetraining():
    harvest_marinetraining()