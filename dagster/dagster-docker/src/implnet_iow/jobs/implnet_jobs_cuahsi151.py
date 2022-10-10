from dagster import job

from ops.implnet_ops_cuahsi151 import harvest_cuahsi151

@job
def implnet_job_cuahsi151():
    harvest_cuahsi151()