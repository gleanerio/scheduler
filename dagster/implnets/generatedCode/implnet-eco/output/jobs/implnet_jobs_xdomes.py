from dagster import job

from ops.implnet_ops_xdomes import harvest_xdomes

@job
def implnet_job_xdomes():
    harvest_xdomes()