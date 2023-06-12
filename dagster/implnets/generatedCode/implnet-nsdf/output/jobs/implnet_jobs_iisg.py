from dagster import job

from ops.implnet_ops_iisg import harvest_iisg

@job
def implnet_job_iisg():
    harvest_iisg()