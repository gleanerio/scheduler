from dagster import job

from ops.implnet_ops_gfv11pois1 import harvest_gfv11pois1

@job
def implnet_job_gfv11pois1():
    harvest_gfv11pois1()