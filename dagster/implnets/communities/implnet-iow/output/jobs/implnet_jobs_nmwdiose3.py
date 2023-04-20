from dagster import job

from ops.implnet_ops_nmwdiose3 import harvest_nmwdiose3

@job
def implnet_job_nmwdiose3():
    harvest_nmwdiose3()