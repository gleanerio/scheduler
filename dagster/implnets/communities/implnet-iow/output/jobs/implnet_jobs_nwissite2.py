from dagster import job

from ops.implnet_ops_nwissite2 import harvest_nwissite2

@job
def implnet_job_nwissite2():
    harvest_nwissite2()