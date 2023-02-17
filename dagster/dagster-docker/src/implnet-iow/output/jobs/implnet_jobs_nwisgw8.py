from dagster import job

from ops.implnet_ops_nwisgw8 import harvest_nwisgw8

@job
def implnet_job_nwisgw8():
    harvest_nwisgw8()