from dagster import job

from ops.implnet_ops_cuahsi109 import harvest_cuahsi109

@job
def implnet_job_cuahsi109():
    harvest_cuahsi109()