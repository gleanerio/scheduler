from dagster import job

from gleaner.ops.implnet_marinetraining import harvest_marinetraining

@job
def implnet_job_marinetraining():
    harvest_marinetraining()