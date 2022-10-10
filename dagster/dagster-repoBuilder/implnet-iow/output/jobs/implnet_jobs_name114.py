from dagster import job

from ops.implnet_ops_name114 import harvest_name114

@job
def implnet_job_name114():
    harvest_name114()