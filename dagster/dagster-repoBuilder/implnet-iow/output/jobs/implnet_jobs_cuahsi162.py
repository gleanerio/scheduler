from dagster import job

from ops.implnet_ops_cuahsi162 import harvest_cuahsi162

@job
def implnet_job_cuahsi162():
    harvest_cuahsi162()