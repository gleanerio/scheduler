from dagster import job

from ops.implnet_ops_vtti import harvest_vtti

@job
def implnet_job_vtti():
    harvest_vtti()