from dagster import job

from gleaner.ops.oih_aquadocs import harvest_aquadocs

@job
def oih_job_aquadocs():
    harvest_aquadocs()