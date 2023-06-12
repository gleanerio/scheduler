from dagster import job

from ops.implnet_ops_rsu import harvest_rsu

@job
def implnet_job_rsu():
    harvest_rsu()