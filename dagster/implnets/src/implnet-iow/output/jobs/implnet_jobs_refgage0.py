from dagster import job

from ops.implnet_ops_refgage0 import harvest_refgage0

@job
def implnet_job_refgage0():
    harvest_refgage0()