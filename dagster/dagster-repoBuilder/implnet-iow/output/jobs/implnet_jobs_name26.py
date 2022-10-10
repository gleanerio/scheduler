from dagster import job

from ops.implnet_ops_name26 import harvest_name26

@job
def implnet_job_name26():
    harvest_name26()