from dagster import job

from ops.implnet_ops_cuahsi101 import harvest_cuahsi101

@job
def implnet_job_cuahsi101():
    harvest_cuahsi101()