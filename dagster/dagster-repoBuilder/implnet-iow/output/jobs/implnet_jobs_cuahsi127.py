from dagster import job

from ops.implnet_ops_cuahsi127 import harvest_cuahsi127

@job
def implnet_job_cuahsi127():
    harvest_cuahsi127()