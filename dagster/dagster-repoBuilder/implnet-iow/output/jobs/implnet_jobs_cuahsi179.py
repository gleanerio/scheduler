from dagster import job

from ops.implnet_ops_cuahsi179 import harvest_cuahsi179

@job
def implnet_job_cuahsi179():
    harvest_cuahsi179()