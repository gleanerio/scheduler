from dagster import job

from ops.implnet_ops_cuahsi160 import harvest_cuahsi160

@job
def implnet_job_cuahsi160():
    harvest_cuahsi160()