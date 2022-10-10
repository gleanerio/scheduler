from dagster import job

from ops.implnet_ops_name103 import harvest_name103

@job
def implnet_job_name103():
    harvest_name103()