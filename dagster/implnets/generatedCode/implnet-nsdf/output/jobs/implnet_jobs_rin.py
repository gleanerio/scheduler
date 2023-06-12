from dagster import job

from ops.implnet_ops_rin import harvest_rin

@job
def implnet_job_rin():
    harvest_rin()