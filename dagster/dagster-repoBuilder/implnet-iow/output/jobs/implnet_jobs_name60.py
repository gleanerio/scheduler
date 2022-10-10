from dagster import job

from ops.implnet_ops_name60 import harvest_name60

@job
def implnet_job_name60():
    harvest_name60()