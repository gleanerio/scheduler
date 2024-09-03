from dagster import job

from ops.implnet_ops_iow_demo__0 import harvest_iow_demo__0

@job
def implnet_job_iow_demo__0():
    harvest_iow_demo__0()
