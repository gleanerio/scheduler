from dagster import job

from ops.implnet_ops_unidata import harvest_unidata

@job
def implnet_job_unidata():
    harvest_unidata()