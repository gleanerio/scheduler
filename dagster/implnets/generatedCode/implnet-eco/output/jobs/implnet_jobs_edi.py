from dagster import job

from ops.implnet_ops_edi import harvest_edi

@job
def implnet_job_edi():
    harvest_edi()