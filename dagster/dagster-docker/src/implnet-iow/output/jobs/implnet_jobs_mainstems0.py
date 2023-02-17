from dagster import job

from ops.implnet_ops_mainstems0 import harvest_mainstems0

@job
def implnet_job_mainstems0():
    harvest_mainstems0()