from dagster import job

from ops.implnet_ops_cuahsi178 import harvest_cuahsi178

@job
def implnet_job_cuahsi178():
    harvest_cuahsi178()