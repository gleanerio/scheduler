from dagster import job

from ops.implnet_ops_ref59 import harvest_ref59

@job
def implnet_job_ref59():
    harvest_ref59()