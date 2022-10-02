from dagster import job

from gleaner.ops.implnet_edmerp import harvest_edmerp

@job
def implnet_job_edmerp():
    harvest_edmerp()