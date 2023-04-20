from dagster import job

from ops.implnet_ops_iedadata import harvest_iedadata

@job
def implnet_job_iedadata():
    harvest_iedadata()