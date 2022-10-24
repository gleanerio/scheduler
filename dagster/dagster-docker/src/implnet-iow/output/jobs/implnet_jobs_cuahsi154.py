from dagster import job

from ops.implnet_ops_cuahsi154 import harvest_cuahsi154

@job
def implnet_job_cuahsi154():
    harvest_cuahsi154()