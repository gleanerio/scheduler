from dagster import job

from ops.implnet_ops_name113 import harvest_name113

@job
def implnet_job_name113():
    harvest_name113()