from dagster import job

from ops.implnet_ops_vliz import harvest_vliz

@job
def implnet_job_vliz():
    harvest_vliz()