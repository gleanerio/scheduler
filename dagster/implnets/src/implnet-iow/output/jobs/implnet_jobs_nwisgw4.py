from dagster import job

from ops.implnet_ops_nwisgw4 import harvest_nwisgw4

@job
def implnet_job_nwisgw4():
    harvest_nwisgw4()