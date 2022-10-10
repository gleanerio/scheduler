from dagster import job

from ops.implnet_ops_name142 import harvest_name142

@job
def implnet_job_name142():
    harvest_name142()