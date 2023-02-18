from dagster import job

from ops.implnet_ops_autotest10 import harvest_autotest10

@job
def implnet_job_autotest10():
    harvest_autotest10()