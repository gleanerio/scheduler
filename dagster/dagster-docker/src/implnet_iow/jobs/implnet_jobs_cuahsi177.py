from dagster import job

from ops.implnet_ops_cuahsi177 import harvest_cuahsi177

@job
def implnet_job_cuahsi177():
    harvest_cuahsi177()