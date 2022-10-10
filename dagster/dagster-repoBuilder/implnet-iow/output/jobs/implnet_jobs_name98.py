from dagster import job

from ops.implnet_ops_name98 import harvest_name98

@job
def implnet_job_name98():
    harvest_name98()