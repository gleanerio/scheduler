from dagster import job

from ops.implnet_ops_name162 import harvest_name162

@job
def implnet_job_name162():
    harvest_name162()