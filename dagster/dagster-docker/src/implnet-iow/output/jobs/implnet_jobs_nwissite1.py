from dagster import job

from ops.implnet_ops_nwissite1 import harvest_nwissite1

@job
def implnet_job_nwissite1():
    harvest_nwissite1()