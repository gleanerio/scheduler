from dagster import job

from ops.implnet_ops_ssdb.iodp import harvest_ssdb.iodp

@job
def implnet_job_ssdb.iodp():
    harvest_ssdb.iodp()