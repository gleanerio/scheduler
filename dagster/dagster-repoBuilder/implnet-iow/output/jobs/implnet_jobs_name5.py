from dagster import job

from ops.implnet_ops_name5 import harvest_name5

@job
def implnet_job_name5():
    harvest_name5()