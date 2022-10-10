from dagster import job

from ops.implnet_ops_cuahsi146 import harvest_cuahsi146

@job
def implnet_job_cuahsi146():
    harvest_cuahsi146()