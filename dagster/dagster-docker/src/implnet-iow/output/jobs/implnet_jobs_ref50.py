from dagster import job

from ops.implnet_ops_ref50 import harvest_ref50

@job
def implnet_job_ref50():
    harvest_ref50()