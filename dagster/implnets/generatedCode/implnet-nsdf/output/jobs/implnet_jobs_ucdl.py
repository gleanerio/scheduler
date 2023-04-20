from dagster import job

from ops.implnet_ops_ucdl import harvest_ucdl

@job
def implnet_job_ucdl():
    harvest_ucdl()