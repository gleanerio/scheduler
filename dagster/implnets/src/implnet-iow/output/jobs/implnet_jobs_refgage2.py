from dagster import job

from ops.implnet_ops_refgage2 import harvest_refgage2

@job
def implnet_job_refgage2():
    harvest_refgage2()