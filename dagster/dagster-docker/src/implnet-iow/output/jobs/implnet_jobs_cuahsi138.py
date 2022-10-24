from dagster import job

from ops.implnet_ops_cuahsi138 import harvest_cuahsi138

@job
def implnet_job_cuahsi138():
    harvest_cuahsi138()