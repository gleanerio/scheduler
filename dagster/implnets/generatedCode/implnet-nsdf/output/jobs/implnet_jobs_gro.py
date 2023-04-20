from dagster import job

from ops.implnet_ops_gro import harvest_gro

@job
def implnet_job_gro():
    harvest_gro()