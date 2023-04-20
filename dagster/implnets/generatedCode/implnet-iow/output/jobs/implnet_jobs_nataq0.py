from dagster import job

from ops.implnet_ops_nataq0 import harvest_nataq0

@job
def implnet_job_nataq0():
    harvest_nataq0()