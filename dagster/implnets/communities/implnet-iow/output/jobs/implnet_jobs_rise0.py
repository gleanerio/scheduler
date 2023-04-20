from dagster import job

from ops.implnet_ops_rise0 import harvest_rise0

@job
def implnet_job_rise0():
    harvest_rise0()