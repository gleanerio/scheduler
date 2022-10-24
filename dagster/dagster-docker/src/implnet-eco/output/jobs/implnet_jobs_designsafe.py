from dagster import job

from ops.implnet_ops_designsafe import harvest_designsafe

@job
def implnet_job_designsafe():
    harvest_designsafe()