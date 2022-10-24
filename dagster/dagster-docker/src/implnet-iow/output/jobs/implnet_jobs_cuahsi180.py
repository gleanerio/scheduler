from dagster import job

from ops.implnet_ops_cuahsi180 import harvest_cuahsi180

@job
def implnet_job_cuahsi180():
    harvest_cuahsi180()