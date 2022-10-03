from dagster import job

from ops.implnet_ops_invemardocuments import harvest_invemardocuments

@job
def implnet_job_invemardocuments():
    harvest_invemardocuments()