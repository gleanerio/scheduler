from dagster import job

from ops.implnet_ops_cuahsi169 import harvest_cuahsi169

@job
def implnet_job_cuahsi169():
    harvest_cuahsi169()