from dagster import job

from ops.implnet_ops_euroceanexperts import harvest_euroceanexperts

@job
def implnet_job_euroceanexperts():
    harvest_euroceanexperts()