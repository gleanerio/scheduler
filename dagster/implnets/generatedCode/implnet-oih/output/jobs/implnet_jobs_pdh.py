from dagster import job

from ops.implnet_ops_pdh import harvest_pdh

@job
def implnet_job_pdh():
    harvest_pdh()