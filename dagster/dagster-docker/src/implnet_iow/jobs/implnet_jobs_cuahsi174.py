from dagster import job

from ops.implnet_ops_cuahsi174 import harvest_cuahsi174

@job
def implnet_job_cuahsi174():
    harvest_cuahsi174()