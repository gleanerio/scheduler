from dagster import job

from ops.implnet_ops_name102 import harvest_name102

@job
def implnet_job_name102():
    harvest_name102()