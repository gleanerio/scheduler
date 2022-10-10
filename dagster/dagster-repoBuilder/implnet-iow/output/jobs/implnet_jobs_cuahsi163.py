from dagster import job

from ops.implnet_ops_cuahsi163 import harvest_cuahsi163

@job
def implnet_job_cuahsi163():
    harvest_cuahsi163()