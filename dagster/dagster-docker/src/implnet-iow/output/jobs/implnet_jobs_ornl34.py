from dagster import job

from ops.implnet_ops_ornl34 import harvest_ornl34

@job
def implnet_job_ornl34():
    harvest_ornl34()