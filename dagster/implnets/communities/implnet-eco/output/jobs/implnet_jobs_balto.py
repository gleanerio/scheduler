from dagster import job

from ops.implnet_ops_balto import harvest_balto

@job
def implnet_job_balto():
    harvest_balto()