from dagster import job

from ops.implnet_ops_cuahsi112 import harvest_cuahsi112

@job
def implnet_job_cuahsi112():
    harvest_cuahsi112()