from dagster import job

from gleaner.ops.oih_edmerp import harvest_edmerp

@job
def oih_job_edmerp():
    harvest_edmerp()