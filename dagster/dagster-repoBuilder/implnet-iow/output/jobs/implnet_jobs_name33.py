from dagster import job

from ops.implnet_ops_name33 import harvest_name33

@job
def implnet_job_name33():
    harvest_name33()