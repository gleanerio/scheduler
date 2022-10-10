from dagster import job

from ops.implnet_ops_name62 import harvest_name62

@job
def implnet_job_name62():
    harvest_name62()