from dagster import job

from ops.implnet_ops_ref61 import harvest_ref61

@job
def implnet_job_ref61():
    harvest_ref61()