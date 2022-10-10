from dagster import job

from ops.implnet_ops_cuahsi98 import harvest_cuahsi98

@job
def implnet_job_cuahsi98():
    harvest_cuahsi98()