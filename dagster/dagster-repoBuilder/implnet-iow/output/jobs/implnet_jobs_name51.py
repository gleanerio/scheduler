from dagster import job

from ops.implnet_ops_name51 import harvest_name51

@job
def implnet_job_name51():
    harvest_name51()