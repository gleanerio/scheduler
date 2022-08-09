from dagster import job

from gleaner.ops.oih_marinetraining import harvest_marinetraining

@job
def oih_job_marinetraining():
    harvest_marinetraining()