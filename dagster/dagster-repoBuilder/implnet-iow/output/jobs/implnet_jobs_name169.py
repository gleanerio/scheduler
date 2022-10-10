from dagster import job

from ops.implnet_ops_name169 import harvest_name169

@job
def implnet_job_name169():
    harvest_name169()