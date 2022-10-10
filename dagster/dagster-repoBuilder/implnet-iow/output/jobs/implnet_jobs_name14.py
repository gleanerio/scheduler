from dagster import job

from ops.implnet_ops_name14 import harvest_name14

@job
def implnet_job_name14():
    harvest_name14()