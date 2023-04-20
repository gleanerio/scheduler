from dagster import job

from ops.implnet_ops_inanodc import harvest_inanodc

@job
def implnet_job_inanodc():
    harvest_inanodc()