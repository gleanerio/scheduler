from dagster import job

from ops.implnet_ops_cuahsi161 import harvest_cuahsi161

@job
def implnet_job_cuahsi161():
    harvest_cuahsi161()