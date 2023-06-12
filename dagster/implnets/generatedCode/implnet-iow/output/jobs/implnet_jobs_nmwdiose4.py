from dagster import job

from ops.implnet_ops_nmwdiose4 import harvest_nmwdiose4

@job
def implnet_job_nmwdiose4():
    harvest_nmwdiose4()