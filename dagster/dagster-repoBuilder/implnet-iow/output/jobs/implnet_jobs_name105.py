from dagster import job

from ops.implnet_ops_name105 import harvest_name105

@job
def implnet_job_name105():
    harvest_name105()