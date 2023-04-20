from dagster import job

from ops.implnet_ops_counties0 import harvest_counties0

@job
def implnet_job_counties0():
    harvest_counties0()