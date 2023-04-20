from dagster import job

from ops.implnet_ops_nwisgw26 import harvest_nwisgw26

@job
def implnet_job_nwisgw26():
    harvest_nwisgw26()