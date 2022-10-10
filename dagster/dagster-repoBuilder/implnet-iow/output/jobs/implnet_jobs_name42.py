from dagster import job

from ops.implnet_ops_name42 import harvest_name42

@job
def implnet_job_name42():
    harvest_name42()