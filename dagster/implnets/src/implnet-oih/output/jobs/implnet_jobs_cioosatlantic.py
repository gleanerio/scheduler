from dagster import job

from ops.implnet_ops_cioosatlantic import harvest_cioosatlantic

@job
def implnet_job_cioosatlantic():
    harvest_cioosatlantic()