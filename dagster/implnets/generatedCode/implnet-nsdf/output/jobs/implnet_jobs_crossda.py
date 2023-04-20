from dagster import job

from ops.implnet_ops_crossda import harvest_crossda

@job
def implnet_job_crossda():
    harvest_crossda()