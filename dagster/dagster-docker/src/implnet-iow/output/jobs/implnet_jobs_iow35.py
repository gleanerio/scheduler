from dagster import job

from ops.implnet_ops_iow35 import harvest_iow35

@job
def implnet_job_iow35():
    harvest_iow35()