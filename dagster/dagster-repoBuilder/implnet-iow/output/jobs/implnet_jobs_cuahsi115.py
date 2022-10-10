from dagster import job

from ops.implnet_ops_cuahsi115 import harvest_cuahsi115

@job
def implnet_job_cuahsi115():
    harvest_cuahsi115()