from dagster import job

from ops.implnet_ops_name141 import harvest_name141

@job
def implnet_job_name141():
    harvest_name141()