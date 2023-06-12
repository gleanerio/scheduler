from dagster import job

from ops.implnet_ops_wade7 import harvest_wade7

@job
def implnet_job_wade7():
    harvest_wade7()