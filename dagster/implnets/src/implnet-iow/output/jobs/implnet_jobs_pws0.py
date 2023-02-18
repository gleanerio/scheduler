from dagster import job

from ops.implnet_ops_pws0 import harvest_pws0

@job
def implnet_job_pws0():
    harvest_pws0()