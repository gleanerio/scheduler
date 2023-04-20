from dagster import job

from ops.implnet_ops_nwisgw15 import harvest_nwisgw15

@job
def implnet_job_nwisgw15():
    harvest_nwisgw15()