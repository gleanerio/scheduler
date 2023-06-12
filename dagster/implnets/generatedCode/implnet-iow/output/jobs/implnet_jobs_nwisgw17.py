from dagster import job

from ops.implnet_ops_nwisgw17 import harvest_nwisgw17

@job
def implnet_job_nwisgw17():
    harvest_nwisgw17()