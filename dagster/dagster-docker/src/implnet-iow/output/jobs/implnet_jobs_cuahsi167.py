from dagster import job

from ops.implnet_ops_cuahsi167 import harvest_cuahsi167

@job
def implnet_job_cuahsi167():
    harvest_cuahsi167()