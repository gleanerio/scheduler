from dagster import job

from ops.implnet_ops_iow37 import harvest_iow37

@job
def implnet_job_iow37():
    harvest_iow37()