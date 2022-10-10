from dagster import job

from ops.implnet_ops_name52 import harvest_name52

@job
def implnet_job_name52():
    harvest_name52()