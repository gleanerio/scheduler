from dagster import job

from ops.implnet_ops_ifdc import harvest_ifdc

@job
def implnet_job_ifdc():
    harvest_ifdc()