from dagster import job

from ops.implnet_ops_cuahsi116 import harvest_cuahsi116

@job
def implnet_job_cuahsi116():
    harvest_cuahsi116()