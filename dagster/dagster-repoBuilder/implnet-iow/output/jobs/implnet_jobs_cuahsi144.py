from dagster import job

from ops.implnet_ops_cuahsi144 import harvest_cuahsi144

@job
def implnet_job_cuahsi144():
    harvest_cuahsi144()