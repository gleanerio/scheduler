from dagster import job

from ops.implnet_ops_cuahsi135 import harvest_cuahsi135

@job
def implnet_job_cuahsi135():
    harvest_cuahsi135()