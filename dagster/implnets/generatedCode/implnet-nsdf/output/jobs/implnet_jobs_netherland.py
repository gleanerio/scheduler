from dagster import job

from ops.implnet_ops_netherland import harvest_netherland

@job
def implnet_job_netherland():
    harvest_netherland()