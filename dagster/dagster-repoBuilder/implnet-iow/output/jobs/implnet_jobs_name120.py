from dagster import job

from ops.implnet_ops_name120 import harvest_name120

@job
def implnet_job_name120():
    harvest_name120()