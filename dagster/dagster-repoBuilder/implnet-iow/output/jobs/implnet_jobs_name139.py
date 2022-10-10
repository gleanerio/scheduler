from dagster import job

from ops.implnet_ops_name139 import harvest_name139

@job
def implnet_job_name139():
    harvest_name139()