from dagster import job

from ops.implnet_ops_ref49 import harvest_ref49

@job
def implnet_job_ref49():
    harvest_ref49()