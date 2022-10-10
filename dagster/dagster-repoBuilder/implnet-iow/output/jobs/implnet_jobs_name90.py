from dagster import job

from ops.implnet_ops_name90 import harvest_name90

@job
def implnet_job_name90():
    harvest_name90()