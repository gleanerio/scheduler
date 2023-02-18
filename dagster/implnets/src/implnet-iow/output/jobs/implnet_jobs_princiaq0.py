from dagster import job

from ops.implnet_ops_princiaq0 import harvest_princiaq0

@job
def implnet_job_princiaq0():
    harvest_princiaq0()