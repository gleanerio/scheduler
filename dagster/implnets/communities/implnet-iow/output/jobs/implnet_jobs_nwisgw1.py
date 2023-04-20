from dagster import job

from ops.implnet_ops_nwisgw1 import harvest_nwisgw1

@job
def implnet_job_nwisgw1():
    harvest_nwisgw1()