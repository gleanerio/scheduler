from dagster import job

from ops.implnet_ops_manitoba import harvest_manitoba

@job
def implnet_job_manitoba():
    harvest_manitoba()