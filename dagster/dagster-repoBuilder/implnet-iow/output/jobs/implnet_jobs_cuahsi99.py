from dagster import job

from ops.implnet_ops_cuahsi99 import harvest_cuahsi99

@job
def implnet_job_cuahsi99():
    harvest_cuahsi99()