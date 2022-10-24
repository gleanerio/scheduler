from dagster import job

from ops.implnet_ops_decade import harvest_decade

@job
def implnet_job_decade():
    harvest_decade()