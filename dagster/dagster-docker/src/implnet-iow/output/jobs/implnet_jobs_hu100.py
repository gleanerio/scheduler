from dagster import job

from ops.implnet_ops_hu100 import harvest_hu100

@job
def implnet_job_hu100():
    harvest_hu100()