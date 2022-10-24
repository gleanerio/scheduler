from dagster import job

from ops.implnet_ops_renci import harvest_renci

@job
def implnet_job_renci():
    harvest_renci()