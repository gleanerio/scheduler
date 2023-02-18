from dagster import job

from ops.implnet_ops_usapdc import harvest_usapdc

@job
def implnet_job_usapdc():
    harvest_usapdc()