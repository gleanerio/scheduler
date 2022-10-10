from dagster import job

from ops.implnet_ops_name112 import harvest_name112

@job
def implnet_job_name112():
    harvest_name112()