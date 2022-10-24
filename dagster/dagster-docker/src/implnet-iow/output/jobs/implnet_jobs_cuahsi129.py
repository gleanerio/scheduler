from dagster import job

from ops.implnet_ops_cuahsi129 import harvest_cuahsi129

@job
def implnet_job_cuahsi129():
    harvest_cuahsi129()