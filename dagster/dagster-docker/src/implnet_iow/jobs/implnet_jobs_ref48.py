from dagster import job

from ops.implnet_ops_ref48 import harvest_ref48

@job
def implnet_job_ref48():
    harvest_ref48()