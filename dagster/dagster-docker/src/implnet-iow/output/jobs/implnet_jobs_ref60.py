from dagster import job

from ops.implnet_ops_ref60 import harvest_ref60

@job
def implnet_job_ref60():
    harvest_ref60()