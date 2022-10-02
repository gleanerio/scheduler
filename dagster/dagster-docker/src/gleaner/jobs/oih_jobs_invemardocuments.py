from dagster import job

from gleaner.ops.oih_invemardocuments import harvest_invemardocuments

@job
def oih_job_invemardocuments():
    harvest_invemardocuments()