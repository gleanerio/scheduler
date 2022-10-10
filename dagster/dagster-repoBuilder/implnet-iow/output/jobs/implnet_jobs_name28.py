from dagster import job

from ops.implnet_ops_name28 import harvest_name28

@job
def implnet_job_name28():
    harvest_name28()