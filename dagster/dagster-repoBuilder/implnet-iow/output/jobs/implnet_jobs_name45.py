from dagster import job

from ops.implnet_ops_name45 import harvest_name45

@job
def implnet_job_name45():
    harvest_name45()