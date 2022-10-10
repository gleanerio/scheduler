from dagster import job

from ops.implnet_ops_ref51 import harvest_ref51

@job
def implnet_job_ref51():
    harvest_ref51()