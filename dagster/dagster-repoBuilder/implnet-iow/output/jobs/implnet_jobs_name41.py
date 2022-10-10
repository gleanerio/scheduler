from dagster import job

from ops.implnet_ops_name41 import harvest_name41

@job
def implnet_job_name41():
    harvest_name41()