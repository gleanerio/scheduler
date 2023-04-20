from dagster import job

from ops.implnet_ops_cimmyt import harvest_cimmyt

@job
def implnet_job_cimmyt():
    harvest_cimmyt()