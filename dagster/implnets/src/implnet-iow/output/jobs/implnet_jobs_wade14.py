from dagster import job

from ops.implnet_ops_wade14 import harvest_wade14

@job
def implnet_job_wade14():
    harvest_wade14()