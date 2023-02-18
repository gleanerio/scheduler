from dagster import job

from ops.implnet_ops_bcodmo import harvest_bcodmo

@job
def implnet_job_bcodmo():
    harvest_bcodmo()