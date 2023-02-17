from dagster import job

from ops.implnet_ops_nwisgw28 import harvest_nwisgw28

@job
def implnet_job_nwisgw28():
    harvest_nwisgw28()