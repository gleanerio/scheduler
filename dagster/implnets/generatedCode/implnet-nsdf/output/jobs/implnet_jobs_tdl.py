from dagster import job

from ops.implnet_ops_tdl import harvest_tdl

@job
def implnet_job_tdl():
    harvest_tdl()