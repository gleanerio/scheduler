from dagster import job

from ops.implnet_ops_fiu import harvest_fiu

@job
def implnet_job_fiu():
    harvest_fiu()