from dagster import job

from ops.implnet_ops_dams1 import harvest_dams1

@job
def implnet_job_dams1():
    harvest_dams1()