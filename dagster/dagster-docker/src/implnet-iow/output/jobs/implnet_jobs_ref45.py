from dagster import job

from ops.implnet_ops_ref45 import harvest_ref45

@job
def implnet_job_ref45():
    harvest_ref45()