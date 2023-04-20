from dagster import job

from ops.implnet_ops_nwisgw21 import harvest_nwisgw21

@job
def implnet_job_nwisgw21():
    harvest_nwisgw21()