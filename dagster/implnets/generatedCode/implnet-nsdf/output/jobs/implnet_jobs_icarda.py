from dagster import job

from ops.implnet_ops_icarda import harvest_icarda

@job
def implnet_job_icarda():
    harvest_icarda()