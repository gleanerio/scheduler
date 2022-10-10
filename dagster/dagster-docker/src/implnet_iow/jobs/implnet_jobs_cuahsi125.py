from dagster import job

from ops.implnet_ops_cuahsi125 import harvest_cuahsi125

@job
def implnet_job_cuahsi125():
    harvest_cuahsi125()