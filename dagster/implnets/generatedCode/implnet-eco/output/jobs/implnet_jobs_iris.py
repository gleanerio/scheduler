from dagster import job

from ops.implnet_ops_iris import harvest_iris

@job
def implnet_job_iris():
    harvest_iris()