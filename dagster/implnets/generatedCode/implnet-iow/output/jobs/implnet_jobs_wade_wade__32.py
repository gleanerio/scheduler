from dagster import job

from ops.implnet_ops_wade_wade__32 import harvest_wade_wade__32

@job
def implnet_job_wade_wade__32():
    harvest_wade_wade__32()
