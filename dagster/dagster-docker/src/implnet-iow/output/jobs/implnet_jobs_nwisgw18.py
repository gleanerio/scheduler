from dagster import job

from ops.implnet_ops_nwisgw18 import harvest_nwisgw18

@job
def implnet_job_nwisgw18():
    harvest_nwisgw18()