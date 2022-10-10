from dagster import job

from ops.implnet_ops_cuahsi156 import harvest_cuahsi156

@job
def implnet_job_cuahsi156():
    harvest_cuahsi156()