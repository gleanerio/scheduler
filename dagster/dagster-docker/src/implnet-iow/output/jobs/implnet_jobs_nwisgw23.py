from dagster import job

from ops.implnet_ops_nwisgw23 import harvest_nwisgw23

@job
def implnet_job_nwisgw23():
    harvest_nwisgw23()