from dagster import job

from ops.implnet_ops_name24 import harvest_name24

@job
def implnet_job_name24():
    harvest_name24()