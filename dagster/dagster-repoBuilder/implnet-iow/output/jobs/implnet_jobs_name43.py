from dagster import job

from ops.implnet_ops_name43 import harvest_name43

@job
def implnet_job_name43():
    harvest_name43()