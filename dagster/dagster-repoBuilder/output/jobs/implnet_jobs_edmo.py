from dagster import job

from ops.implnet_ops_edmo import harvest_edmo

@job
def implnet_job_edmo():
    harvest_edmo()