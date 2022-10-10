from dagster import job

from ops.implnet_ops_name1 import harvest_name1

@job
def implnet_job_name1():
    harvest_name1()