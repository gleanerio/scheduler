from dagster import job

from ops.implnet_ops_cuahsi111 import harvest_cuahsi111

@job
def implnet_job_cuahsi111():
    harvest_cuahsi111()