from dagster import job

from ops.implnet_ops_ref56 import harvest_ref56

@job
def implnet_job_ref56():
    harvest_ref56()