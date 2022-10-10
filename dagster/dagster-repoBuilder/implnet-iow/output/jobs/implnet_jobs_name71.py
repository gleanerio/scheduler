from dagster import job

from ops.implnet_ops_name71 import harvest_name71

@job
def implnet_job_name71():
    harvest_name71()