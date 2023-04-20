from dagster import job

from ops.implnet_ops_aquadocs import harvest_aquadocs

@job
def implnet_job_aquadocs():
    harvest_aquadocs()