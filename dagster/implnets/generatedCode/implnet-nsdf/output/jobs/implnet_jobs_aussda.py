from dagster import job

from ops.implnet_ops_aussda import harvest_aussda

@job
def implnet_job_aussda():
    harvest_aussda()