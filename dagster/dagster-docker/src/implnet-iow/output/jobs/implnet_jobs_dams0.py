from dagster import job

from ops.implnet_ops_dams0 import harvest_dams0

@job
def implnet_job_dams0():
    harvest_dams0()