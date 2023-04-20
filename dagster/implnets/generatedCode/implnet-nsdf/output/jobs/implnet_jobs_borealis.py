from dagster import job

from ops.implnet_ops_borealis import harvest_borealis

@job
def implnet_job_borealis():
    harvest_borealis()