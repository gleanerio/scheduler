from dagster import job

from ops.implnet_ops_nwisgw12 import harvest_nwisgw12

@job
def implnet_job_nwisgw12():
    harvest_nwisgw12()