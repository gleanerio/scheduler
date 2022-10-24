from dagster import job

from ops.implnet_ops_ref40 import harvest_ref40

@job
def implnet_job_ref40():
    harvest_ref40()