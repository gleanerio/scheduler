from dagster import job

from ops.implnet_ops_name73 import harvest_name73

@job
def implnet_job_name73():
    harvest_name73()