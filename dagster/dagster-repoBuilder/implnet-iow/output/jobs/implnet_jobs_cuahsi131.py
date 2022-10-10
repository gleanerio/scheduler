from dagster import job

from ops.implnet_ops_cuahsi131 import harvest_cuahsi131

@job
def implnet_job_cuahsi131():
    harvest_cuahsi131()