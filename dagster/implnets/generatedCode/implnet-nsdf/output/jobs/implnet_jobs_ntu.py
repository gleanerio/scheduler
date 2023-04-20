from dagster import job

from ops.implnet_ops_ntu import harvest_ntu

@job
def implnet_job_ntu():
    harvest_ntu()