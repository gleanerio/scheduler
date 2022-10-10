from dagster import job

from ops.implnet_ops_cuahsi171 import harvest_cuahsi171

@job
def implnet_job_cuahsi171():
    harvest_cuahsi171()