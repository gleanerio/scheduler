from dagster import job

from ops.implnet_ops_adf import harvest_adf

@job
def implnet_job_adf():
    harvest_adf()