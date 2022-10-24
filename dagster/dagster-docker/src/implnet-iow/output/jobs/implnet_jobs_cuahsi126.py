from dagster import job

from ops.implnet_ops_cuahsi126 import harvest_cuahsi126

@job
def implnet_job_cuahsi126():
    harvest_cuahsi126()