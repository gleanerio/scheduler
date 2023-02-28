from dagster import job

from ops.implnet_ops_pogo import harvest_pogo

@job
def implnet_job_pogo():
    harvest_pogo()