from dagster import job

from ops.implnet_ops_name89 import harvest_name89

@job
def implnet_job_name89():
    harvest_name89()