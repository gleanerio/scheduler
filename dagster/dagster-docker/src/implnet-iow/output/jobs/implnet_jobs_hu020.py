from dagster import job

from ops.implnet_ops_hu020 import harvest_hu020

@job
def implnet_job_hu020():
    harvest_hu020()