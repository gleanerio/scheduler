from dagster import job

from ops.implnet_ops_name128 import harvest_name128

@job
def implnet_job_name128():
    harvest_name128()