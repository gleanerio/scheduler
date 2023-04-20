from dagster import job

from ops.implnet_ops_nwissite3 import harvest_nwissite3

@job
def implnet_job_nwissite3():
    harvest_nwissite3()