from dagster import job

from ops.implnet_ops_cuahsi136 import harvest_cuahsi136

@job
def implnet_job_cuahsi136():
    harvest_cuahsi136()