from dagster import job

from ops.implnet_ops_wade13 import harvest_wade13

@job
def implnet_job_wade13():
    harvest_wade13()