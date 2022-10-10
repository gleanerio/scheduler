from dagster import job

from ops.implnet_ops_cuahsi157 import harvest_cuahsi157

@job
def implnet_job_cuahsi157():
    harvest_cuahsi157()