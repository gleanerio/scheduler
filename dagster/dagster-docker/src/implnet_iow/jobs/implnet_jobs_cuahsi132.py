from dagster import job

from ops.implnet_ops_cuahsi132 import harvest_cuahsi132

@job
def implnet_job_cuahsi132():
    harvest_cuahsi132()