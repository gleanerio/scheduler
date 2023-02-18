from dagster import job

from ops.implnet_ops_nwisgw6 import harvest_nwisgw6

@job
def implnet_job_nwisgw6():
    harvest_nwisgw6()