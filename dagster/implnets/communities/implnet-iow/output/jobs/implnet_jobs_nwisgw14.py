from dagster import job

from ops.implnet_ops_nwisgw14 import harvest_nwisgw14

@job
def implnet_job_nwisgw14():
    harvest_nwisgw14()