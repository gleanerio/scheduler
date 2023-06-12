from dagster import job

from ops.implnet_ops_nwisgw3 import harvest_nwisgw3

@job
def implnet_job_nwisgw3():
    harvest_nwisgw3()