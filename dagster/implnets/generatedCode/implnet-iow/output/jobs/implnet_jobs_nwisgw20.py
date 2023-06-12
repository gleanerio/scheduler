from dagster import job

from ops.implnet_ops_nwisgw20 import harvest_nwisgw20

@job
def implnet_job_nwisgw20():
    harvest_nwisgw20()