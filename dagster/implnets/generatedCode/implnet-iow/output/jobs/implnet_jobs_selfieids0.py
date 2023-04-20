from dagster import job

from ops.implnet_ops_selfieids0 import harvest_selfieids0

@job
def implnet_job_selfieids0():
    harvest_selfieids0()