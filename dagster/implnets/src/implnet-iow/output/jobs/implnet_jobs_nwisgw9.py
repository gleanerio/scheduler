from dagster import job

from ops.implnet_ops_nwisgw9 import harvest_nwisgw9

@job
def implnet_job_nwisgw9():
    harvest_nwisgw9()