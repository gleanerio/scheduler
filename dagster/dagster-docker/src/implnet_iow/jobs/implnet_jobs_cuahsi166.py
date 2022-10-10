from dagster import job

from ops.implnet_ops_cuahsi166 import harvest_cuahsi166

@job
def implnet_job_cuahsi166():
    harvest_cuahsi166()