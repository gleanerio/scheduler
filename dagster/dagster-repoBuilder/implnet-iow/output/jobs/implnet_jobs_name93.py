from dagster import job

from ops.implnet_ops_name93 import harvest_name93

@job
def implnet_job_name93():
    harvest_name93()