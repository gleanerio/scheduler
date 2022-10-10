from dagster import job

from ops.implnet_ops_nhdplusv232 import harvest_nhdplusv232

@job
def implnet_job_nhdplusv232():
    harvest_nhdplusv232()