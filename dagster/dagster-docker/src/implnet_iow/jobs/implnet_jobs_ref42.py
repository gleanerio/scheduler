from dagster import job

from ops.implnet_ops_ref42 import harvest_ref42

@job
def implnet_job_ref42():
    harvest_ref42()