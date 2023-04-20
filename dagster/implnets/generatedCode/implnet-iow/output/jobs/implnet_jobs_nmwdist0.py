from dagster import job

from ops.implnet_ops_nmwdist0 import harvest_nmwdist0

@job
def implnet_job_nmwdist0():
    harvest_nmwdist0()