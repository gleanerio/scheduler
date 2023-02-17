from dagster import job

from ops.implnet_ops_nwisgw25 import harvest_nwisgw25

@job
def implnet_job_nwisgw25():
    harvest_nwisgw25()