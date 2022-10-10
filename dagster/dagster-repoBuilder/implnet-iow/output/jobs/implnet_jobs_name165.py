from dagster import job

from ops.implnet_ops_name165 import harvest_name165

@job
def implnet_job_name165():
    harvest_name165()