from dagster import job

from ops.implnet_ops_nwissite0 import harvest_nwissite0

@job
def implnet_job_nwissite0():
    harvest_nwissite0()