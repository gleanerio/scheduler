from dagster import job

from ops.implnet_ops_name138 import harvest_name138

@job
def implnet_job_name138():
    harvest_name138()