from dagster import job

from ops.implnet_ops_opentopography import harvest_opentopography

@job
def implnet_job_opentopography():
    harvest_opentopography()