from dagster import job

from ops.implnet_ops_wade18 import harvest_wade18

@job
def implnet_job_wade18():
    harvest_wade18()