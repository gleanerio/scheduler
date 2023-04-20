from dagster import job

from ops.implnet_ops_maspawio import harvest_maspawio

@job
def implnet_job_maspawio():
    harvest_maspawio()