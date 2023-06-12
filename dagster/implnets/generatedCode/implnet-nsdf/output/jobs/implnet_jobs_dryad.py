from dagster import job

from ops.implnet_ops_dryad import harvest_dryad

@job
def implnet_job_dryad():
    harvest_dryad()