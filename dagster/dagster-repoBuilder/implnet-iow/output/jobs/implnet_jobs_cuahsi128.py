from dagster import job

from ops.implnet_ops_cuahsi128 import harvest_cuahsi128

@job
def implnet_job_cuahsi128():
    harvest_cuahsi128()