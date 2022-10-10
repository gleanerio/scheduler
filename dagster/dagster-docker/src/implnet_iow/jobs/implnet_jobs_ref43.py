from dagster import job

from ops.implnet_ops_ref43 import harvest_ref43

@job
def implnet_job_ref43():
    harvest_ref43()