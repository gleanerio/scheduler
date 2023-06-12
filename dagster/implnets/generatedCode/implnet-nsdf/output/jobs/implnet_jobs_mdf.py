from dagster import job

from ops.implnet_ops_mdf import harvest_mdf

@job
def implnet_job_mdf():
    harvest_mdf()