from dagster import job

from ops.implnet_ops_nwisgw0 import harvest_nwisgw0

@job
def implnet_job_nwisgw0():
    harvest_nwisgw0()