from dagster import job

from ops.implnet_ops_name132 import harvest_name132

@job
def implnet_job_name132():
    harvest_name132()