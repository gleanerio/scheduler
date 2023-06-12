from dagster import job

from ops.implnet_ops_tdi import harvest_tdi

@job
def implnet_job_tdi():
    harvest_tdi()