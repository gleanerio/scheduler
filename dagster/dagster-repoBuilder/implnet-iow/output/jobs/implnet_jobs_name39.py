from dagster import job

from ops.implnet_ops_name39 import harvest_name39

@job
def implnet_job_name39():
    harvest_name39()