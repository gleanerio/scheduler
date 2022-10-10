from dagster import job

from ops.implnet_ops_cuahsi102 import harvest_cuahsi102

@job
def implnet_job_cuahsi102():
    harvest_cuahsi102()