from dagster import job

from ops.implnet_ops_nwisgw13 import harvest_nwisgw13

@job
def implnet_job_nwisgw13():
    harvest_nwisgw13()