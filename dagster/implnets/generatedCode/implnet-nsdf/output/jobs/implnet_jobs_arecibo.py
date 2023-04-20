from dagster import job

from ops.implnet_ops_arecibo import harvest_arecibo

@job
def implnet_job_arecibo():
    harvest_arecibo()