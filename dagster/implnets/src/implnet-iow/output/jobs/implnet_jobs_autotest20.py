from dagster import job

from ops.implnet_ops_autotest20 import harvest_autotest20

@job
def implnet_job_autotest20():
    harvest_autotest20()