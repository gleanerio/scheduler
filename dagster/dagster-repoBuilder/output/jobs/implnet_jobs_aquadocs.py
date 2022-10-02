from dagster import job

from gleaner.ops.implnet_aquadocs import harvest_aquadocs

@job
def implnet_job_aquadocs():
    harvest_aquadocs()