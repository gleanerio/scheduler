from dagster import job

from ops.implnet_ops_wade0 import harvest_wade0

@job
def implnet_job_wade0():
    harvest_wade0()