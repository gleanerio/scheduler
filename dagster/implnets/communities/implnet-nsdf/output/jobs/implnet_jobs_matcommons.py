from dagster import job

from ops.implnet_ops_matcommons import harvest_matcommons

@job
def implnet_job_matcommons():
    harvest_matcommons()