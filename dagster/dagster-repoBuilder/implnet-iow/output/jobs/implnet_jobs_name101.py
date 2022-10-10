from dagster import job

from ops.implnet_ops_name101 import harvest_name101

@job
def implnet_job_name101():
    harvest_name101()