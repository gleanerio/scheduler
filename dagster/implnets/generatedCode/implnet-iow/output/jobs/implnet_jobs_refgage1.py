from dagster import job

from ops.implnet_ops_refgage1 import harvest_refgage1

@job
def implnet_job_refgage1():
    harvest_refgage1()