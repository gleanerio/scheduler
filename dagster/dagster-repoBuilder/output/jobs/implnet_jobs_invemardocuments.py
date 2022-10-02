from dagster import job

from gleaner.ops.implnet_invemardocuments import harvest_invemardocuments

@job
def implnet_job_invemardocuments():
    harvest_invemardocuments()