from dagster import job

from ops.implnet_ops_cbsa0 import harvest_cbsa0

@job
def implnet_job_cbsa0():
    harvest_cbsa0()