from dagster import job

from ops.implnet_ops_cuahsi122 import harvest_cuahsi122

@job
def implnet_job_cuahsi122():
    harvest_cuahsi122()