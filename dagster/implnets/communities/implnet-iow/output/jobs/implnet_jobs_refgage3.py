from dagster import job

from ops.implnet_ops_refgage3 import harvest_refgage3

@job
def implnet_job_refgage3():
    harvest_refgage3()