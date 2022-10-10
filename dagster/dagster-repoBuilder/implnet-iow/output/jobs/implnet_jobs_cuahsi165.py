from dagster import job

from ops.implnet_ops_cuahsi165 import harvest_cuahsi165

@job
def implnet_job_cuahsi165():
    harvest_cuahsi165()