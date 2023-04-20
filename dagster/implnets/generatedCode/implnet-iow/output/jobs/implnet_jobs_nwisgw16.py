from dagster import job

from ops.implnet_ops_nwisgw16 import harvest_nwisgw16

@job
def implnet_job_nwisgw16():
    harvest_nwisgw16()