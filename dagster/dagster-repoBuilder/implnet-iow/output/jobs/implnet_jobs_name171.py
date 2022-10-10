from dagster import job

from ops.implnet_ops_name171 import harvest_name171

@job
def implnet_job_name171():
    harvest_name171()