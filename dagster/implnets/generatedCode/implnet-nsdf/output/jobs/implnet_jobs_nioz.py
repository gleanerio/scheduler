from dagster import job

from ops.implnet_ops_nioz import harvest_nioz

@job
def implnet_job_nioz():
    harvest_nioz()