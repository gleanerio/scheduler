from dagster import job

from ops.implnet_ops_ref41 import harvest_ref41

@job
def implnet_job_ref41():
    harvest_ref41()