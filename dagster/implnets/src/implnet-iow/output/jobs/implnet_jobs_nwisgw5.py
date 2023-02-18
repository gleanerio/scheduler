from dagster import job

from ops.implnet_ops_nwisgw5 import harvest_nwisgw5

@job
def implnet_job_nwisgw5():
    harvest_nwisgw5()