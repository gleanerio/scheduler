from dagster import job

from ops.implnet_ops_iow36 import harvest_iow36

@job
def implnet_job_iow36():
    harvest_iow36()