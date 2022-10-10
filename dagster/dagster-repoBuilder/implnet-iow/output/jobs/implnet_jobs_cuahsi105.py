from dagster import job

from ops.implnet_ops_cuahsi105 import harvest_cuahsi105

@job
def implnet_job_cuahsi105():
    harvest_cuahsi105()