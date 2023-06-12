from dagster import job

from ops.implnet_ops_chile import harvest_chile

@job
def implnet_job_chile():
    harvest_chile()