from dagster import job

from ops.implnet_ops_edmerp import harvest_edmerp

@job
def implnet_job_edmerp():
    harvest_edmerp()