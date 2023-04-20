from dagster import job

from ops.implnet_ops_sceincespo import harvest_sceincespo

@job
def implnet_job_sceincespo():
    harvest_sceincespo()