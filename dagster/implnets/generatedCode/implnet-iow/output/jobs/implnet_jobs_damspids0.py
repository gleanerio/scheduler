from dagster import job

from ops.implnet_ops_damspids0 import harvest_damspids0

@job
def implnet_job_damspids0():
    harvest_damspids0()