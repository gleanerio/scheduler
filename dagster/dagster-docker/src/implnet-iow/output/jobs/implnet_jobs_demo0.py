from dagster import job

from ops.implnet_ops_demo0 import harvest_demo0

@job
def implnet_job_demo0():
    harvest_demo0()