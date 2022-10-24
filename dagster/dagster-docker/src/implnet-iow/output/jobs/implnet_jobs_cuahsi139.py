from dagster import job

from ops.implnet_ops_cuahsi139 import harvest_cuahsi139

@job
def implnet_job_cuahsi139():
    harvest_cuahsi139()