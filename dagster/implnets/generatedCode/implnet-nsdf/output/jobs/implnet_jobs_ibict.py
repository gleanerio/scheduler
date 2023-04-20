from dagster import job

from ops.implnet_ops_ibict import harvest_ibict

@job
def implnet_job_ibict():
    harvest_ibict()