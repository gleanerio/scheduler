from dagster import job

from ops.implnet_ops_cora import harvest_cora

@job
def implnet_job_cora():
    harvest_cora()