from dagster import job

from ops.implnet_ops_cuahsi137 import harvest_cuahsi137

@job
def implnet_job_cuahsi137():
    harvest_cuahsi137()