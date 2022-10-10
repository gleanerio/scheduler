from dagster import job

from ops.implnet_ops_name86 import harvest_name86

@job
def implnet_job_name86():
    harvest_name86()