from dagster import job

from ops.implnet_ops_lida import harvest_lida

@job
def implnet_job_lida():
    harvest_lida()