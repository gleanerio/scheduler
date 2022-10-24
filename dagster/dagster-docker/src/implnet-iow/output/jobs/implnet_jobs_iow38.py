from dagster import job

from ops.implnet_ops_iow38 import harvest_iow38

@job
def implnet_job_iow38():
    harvest_iow38()