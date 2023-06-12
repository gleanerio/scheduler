from dagster import job

from ops.implnet_ops_nmwdiose2 import harvest_nmwdiose2

@job
def implnet_job_nmwdiose2():
    harvest_nmwdiose2()