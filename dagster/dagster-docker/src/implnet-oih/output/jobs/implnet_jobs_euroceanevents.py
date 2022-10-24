from dagster import job

from ops.implnet_ops_euroceanevents import harvest_euroceanevents

@job
def implnet_job_euroceanevents():
    harvest_euroceanevents()