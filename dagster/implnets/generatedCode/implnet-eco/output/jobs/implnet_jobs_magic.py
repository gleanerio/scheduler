from dagster import job

from ops.implnet_ops_magic import harvest_magic

@job
def implnet_job_magic():
    harvest_magic()