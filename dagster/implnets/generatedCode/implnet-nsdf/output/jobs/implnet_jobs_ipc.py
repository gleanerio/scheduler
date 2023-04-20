from dagster import job

from ops.implnet_ops_ipc import harvest_ipc

@job
def implnet_job_ipc():
    harvest_ipc()