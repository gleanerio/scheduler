from dagster import job

from ops.implnet_ops_name10 import harvest_name10

@job
def implnet_job_name10():
    harvest_name10()