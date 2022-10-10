from dagster import job

from ops.implnet_ops_cuahsi124 import harvest_cuahsi124

@job
def implnet_job_cuahsi124():
    harvest_cuahsi124()