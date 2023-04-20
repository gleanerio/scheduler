from dagster import job

from ops.implnet_ops_unavco import harvest_unavco

@job
def implnet_job_unavco():
    harvest_unavco()