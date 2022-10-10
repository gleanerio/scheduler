from dagster import job

from ops.implnet_ops_name21 import harvest_name21

@job
def implnet_job_name21():
    harvest_name21()