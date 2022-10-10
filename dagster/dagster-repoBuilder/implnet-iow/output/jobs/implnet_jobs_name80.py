from dagster import job

from ops.implnet_ops_name80 import harvest_name80

@job
def implnet_job_name80():
    harvest_name80()