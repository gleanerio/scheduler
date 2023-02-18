from dagster import job

from ops.implnet_ops_cchdo import harvest_cchdo

@job
def implnet_job_cchdo():
    harvest_cchdo()