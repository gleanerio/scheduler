from dagster import job

from ops.implnet_ops_wade10 import harvest_wade10

@job
def implnet_job_wade10():
    harvest_wade10()