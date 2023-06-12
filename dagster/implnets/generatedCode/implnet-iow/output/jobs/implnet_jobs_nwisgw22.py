from dagster import job

from ops.implnet_ops_nwisgw22 import harvest_nwisgw22

@job
def implnet_job_nwisgw22():
    harvest_nwisgw22()