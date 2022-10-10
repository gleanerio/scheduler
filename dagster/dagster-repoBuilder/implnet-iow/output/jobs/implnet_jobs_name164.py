from dagster import job

from ops.implnet_ops_name164 import harvest_name164

@job
def implnet_job_name164():
    harvest_name164()