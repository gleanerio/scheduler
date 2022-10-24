from dagster import job

from ops.implnet_ops_epa29 import harvest_epa29

@job
def implnet_job_epa29():
    harvest_epa29()