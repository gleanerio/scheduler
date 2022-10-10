from dagster import job

from ops.implnet_ops_name99 import harvest_name99

@job
def implnet_job_name99():
    harvest_name99()