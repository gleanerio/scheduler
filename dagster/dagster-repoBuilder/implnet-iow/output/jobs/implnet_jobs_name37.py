from dagster import job

from ops.implnet_ops_name37 import harvest_name37

@job
def implnet_job_name37():
    harvest_name37()