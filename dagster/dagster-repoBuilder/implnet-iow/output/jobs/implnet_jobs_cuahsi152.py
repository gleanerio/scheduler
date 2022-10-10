from dagster import job

from ops.implnet_ops_cuahsi152 import harvest_cuahsi152

@job
def implnet_job_cuahsi152():
    harvest_cuahsi152()