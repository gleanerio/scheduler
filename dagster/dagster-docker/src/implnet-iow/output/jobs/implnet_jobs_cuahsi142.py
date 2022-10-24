from dagster import job

from ops.implnet_ops_cuahsi142 import harvest_cuahsi142

@job
def implnet_job_cuahsi142():
    harvest_cuahsi142()