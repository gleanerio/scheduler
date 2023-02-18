from dagster import job

from ops.implnet_ops_nwisgw10 import harvest_nwisgw10

@job
def implnet_job_nwisgw10():
    harvest_nwisgw10()