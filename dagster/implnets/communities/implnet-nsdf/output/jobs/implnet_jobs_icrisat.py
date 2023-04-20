from dagster import job

from ops.implnet_ops_icrisat import harvest_icrisat

@job
def implnet_job_icrisat():
    harvest_icrisat()