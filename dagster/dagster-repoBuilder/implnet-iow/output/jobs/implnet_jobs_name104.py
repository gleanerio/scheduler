from dagster import job

from ops.implnet_ops_name104 import harvest_name104

@job
def implnet_job_name104():
    harvest_name104()