from dagster import job

from ops.implnet_ops_name133 import harvest_name133

@job
def implnet_job_name133():
    harvest_name133()