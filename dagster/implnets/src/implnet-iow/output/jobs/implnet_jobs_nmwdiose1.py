from dagster import job

from ops.implnet_ops_nmwdiose1 import harvest_nmwdiose1

@job
def implnet_job_nmwdiose1():
    harvest_nmwdiose1()