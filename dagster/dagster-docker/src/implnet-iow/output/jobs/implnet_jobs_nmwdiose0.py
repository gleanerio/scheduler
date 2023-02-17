from dagster import job

from ops.implnet_ops_nmwdiose0 import harvest_nmwdiose0

@job
def implnet_job_nmwdiose0():
    harvest_nmwdiose0()