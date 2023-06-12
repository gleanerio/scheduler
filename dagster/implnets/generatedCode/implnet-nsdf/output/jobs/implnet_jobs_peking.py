from dagster import job

from ops.implnet_ops_peking import harvest_peking

@job
def implnet_job_peking():
    harvest_peking()