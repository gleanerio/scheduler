from dagster import job

from ops.implnet_ops_qdr import harvest_qdr

@job
def implnet_job_qdr():
    harvest_qdr()