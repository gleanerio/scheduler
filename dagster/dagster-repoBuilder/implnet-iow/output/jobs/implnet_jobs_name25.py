from dagster import job

from ops.implnet_ops_name25 import harvest_name25

@job
def implnet_job_name25():
    harvest_name25()