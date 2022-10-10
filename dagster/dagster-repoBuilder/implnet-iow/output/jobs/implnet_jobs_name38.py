from dagster import job

from ops.implnet_ops_name38 import harvest_name38

@job
def implnet_job_name38():
    harvest_name38()