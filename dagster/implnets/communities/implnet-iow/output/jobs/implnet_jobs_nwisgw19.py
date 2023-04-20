from dagster import job

from ops.implnet_ops_nwisgw19 import harvest_nwisgw19

@job
def implnet_job_nwisgw19():
    harvest_nwisgw19()