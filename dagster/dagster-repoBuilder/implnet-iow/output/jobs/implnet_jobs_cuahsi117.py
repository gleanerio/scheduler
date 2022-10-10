from dagster import job

from ops.implnet_ops_cuahsi117 import harvest_cuahsi117

@job
def implnet_job_cuahsi117():
    harvest_cuahsi117()