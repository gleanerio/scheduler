from dagster import job

from ops.implnet_ops_cuahsi123 import harvest_cuahsi123

@job
def implnet_job_cuahsi123():
    harvest_cuahsi123()