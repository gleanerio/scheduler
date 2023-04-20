from dagster import job

from ops.implnet_ops_pucdp import harvest_pucdp

@job
def implnet_job_pucdp():
    harvest_pucdp()