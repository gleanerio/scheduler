from dagster import job

from ops.implnet_ops_nwisgw2 import harvest_nwisgw2

@job
def implnet_job_nwisgw2():
    harvest_nwisgw2()