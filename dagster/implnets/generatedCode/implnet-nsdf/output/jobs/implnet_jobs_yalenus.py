from dagster import job

from ops.implnet_ops_yalenus import harvest_yalenus

@job
def implnet_job_yalenus():
    harvest_yalenus()