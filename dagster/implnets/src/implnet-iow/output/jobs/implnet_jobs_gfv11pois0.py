from dagster import job

from ops.implnet_ops_gfv11pois0 import harvest_gfv11pois0

@job
def implnet_job_gfv11pois0():
    harvest_gfv11pois0()