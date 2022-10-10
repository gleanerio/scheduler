from dagster import job

from ops.implnet_ops_name50 import harvest_name50

@job
def implnet_job_name50():
    harvest_name50()