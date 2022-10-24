from dagster import job

from ops.implnet_ops_wade9 import harvest_wade9

@job
def implnet_job_wade9():
    harvest_wade9()