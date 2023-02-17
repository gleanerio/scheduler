from dagster import job

from ops.implnet_ops_nwisgw24 import harvest_nwisgw24

@job
def implnet_job_nwisgw24():
    harvest_nwisgw24()