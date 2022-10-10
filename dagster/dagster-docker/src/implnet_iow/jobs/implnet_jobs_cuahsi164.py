from dagster import job

from ops.implnet_ops_cuahsi164 import harvest_cuahsi164

@job
def implnet_job_cuahsi164():
    harvest_cuahsi164()