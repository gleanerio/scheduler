from dagster import job

from ops.implnet_ops_irl import harvest_irl

@job
def implnet_job_irl():
    harvest_irl()