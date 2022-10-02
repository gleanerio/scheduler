from dagster import job

from gleaner.ops.implnet_nodcid import harvest_nodcid

@job
def implnet_job_nodcid():
    harvest_nodcid()