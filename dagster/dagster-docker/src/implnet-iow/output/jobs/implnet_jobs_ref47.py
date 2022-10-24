from dagster import job

from ops.implnet_ops_ref47 import harvest_ref47

@job
def implnet_job_ref47():
    harvest_ref47()