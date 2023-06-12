from dagster import job

from ops.implnet_ops_oceanexperts import harvest_oceanexperts

@job
def implnet_job_oceanexperts():
    harvest_oceanexperts()