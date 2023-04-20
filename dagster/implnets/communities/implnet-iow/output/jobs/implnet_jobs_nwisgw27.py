from dagster import job

from ops.implnet_ops_nwisgw27 import harvest_nwisgw27

@job
def implnet_job_nwisgw27():
    harvest_nwisgw27()