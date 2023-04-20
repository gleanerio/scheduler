from dagster import job

from ops.implnet_ops_places0 import harvest_places0

@job
def implnet_job_places0():
    harvest_places0()