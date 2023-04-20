from dagster import job

from ops.implnet_ops_edatos import harvest_edatos

@job
def implnet_job_edatos():
    harvest_edatos()