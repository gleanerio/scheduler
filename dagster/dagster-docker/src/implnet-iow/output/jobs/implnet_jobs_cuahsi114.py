from dagster import job

from ops.implnet_ops_cuahsi114 import harvest_cuahsi114

@job
def implnet_job_cuahsi114():
    harvest_cuahsi114()