from dagster import job

from ops.implnet_ops_name19 import harvest_name19

@job
def implnet_job_name19():
    harvest_name19()