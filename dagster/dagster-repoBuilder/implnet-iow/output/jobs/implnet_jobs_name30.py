from dagster import job

from ops.implnet_ops_name30 import harvest_name30

@job
def implnet_job_name30():
    harvest_name30()