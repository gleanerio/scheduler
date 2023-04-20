from dagster import job

from ops.implnet_ops_nwisgw11 import harvest_nwisgw11

@job
def implnet_job_nwisgw11():
    harvest_nwisgw11()