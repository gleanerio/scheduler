from dagster import job

from ops.implnet_ops_neon import harvest_neon

@job
def implnet_job_neon():
    harvest_neon()