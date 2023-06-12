from dagster import job

from ops.implnet_ops_africaioc import harvest_africaioc

@job
def implnet_job_africaioc():
    harvest_africaioc()