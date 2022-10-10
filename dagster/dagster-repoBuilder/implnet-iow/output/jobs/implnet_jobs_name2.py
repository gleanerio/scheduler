from dagster import job

from ops.implnet_ops_name2 import harvest_name2

@job
def implnet_job_name2():
    harvest_name2()