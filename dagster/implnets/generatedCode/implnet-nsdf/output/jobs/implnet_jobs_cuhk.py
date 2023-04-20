from dagster import job

from ops.implnet_ops_cuhk import harvest_cuhk

@job
def implnet_job_cuhk():
    harvest_cuhk()