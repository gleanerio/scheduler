from dagster import job

from ops.implnet_ops_wade5 import harvest_wade5

@job
def implnet_job_wade5():
    harvest_wade5()