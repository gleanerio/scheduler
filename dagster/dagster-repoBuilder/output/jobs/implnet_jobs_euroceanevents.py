from dagster import job

from gleaner.ops.implnet_euroceanevents import harvest_euroceanevents

@job
def implnet_job_euroceanevents():
    harvest_euroceanevents()