from dagster import job

from ops.implnet_ops_norway import harvest_norway

@job
def implnet_job_norway():
    harvest_norway()