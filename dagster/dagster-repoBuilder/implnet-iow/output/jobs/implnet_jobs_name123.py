from dagster import job

from ops.implnet_ops_name123 import harvest_name123

@job
def implnet_job_name123():
    harvest_name123()