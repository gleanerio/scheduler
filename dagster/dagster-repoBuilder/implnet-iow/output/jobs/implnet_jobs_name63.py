from dagster import job

from ops.implnet_ops_name63 import harvest_name63

@job
def implnet_job_name63():
    harvest_name63()