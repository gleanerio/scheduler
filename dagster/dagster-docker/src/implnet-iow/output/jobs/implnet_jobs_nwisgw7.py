from dagster import job

from ops.implnet_ops_nwisgw7 import harvest_nwisgw7

@job
def implnet_job_nwisgw7():
    harvest_nwisgw7()