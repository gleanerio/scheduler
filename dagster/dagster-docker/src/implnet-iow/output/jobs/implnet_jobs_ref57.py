from dagster import job

from ops.implnet_ops_ref57 import harvest_ref57

@job
def implnet_job_ref57():
    harvest_ref57()