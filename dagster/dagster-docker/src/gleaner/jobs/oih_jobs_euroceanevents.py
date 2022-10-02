from dagster import job

from gleaner.ops.oih_euroceanevents import harvest_euroceanevents

@job
def oih_job_euroceanevents():
    harvest_euroceanevents()