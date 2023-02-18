from dagster import job

from ops.implnet_ops_ucar import harvest_ucar

@job
def implnet_job_ucar():
    harvest_ucar()